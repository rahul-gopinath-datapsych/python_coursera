import pandas as pd
import numpy as np
import os
import datetime as dt
from datetime import date , time
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mp


class dataassertionreport:
#         '''
#         Function does Sanitcy Check on the dataframe to look for data consistency and accuracy
#         '''
    def __init__(self, dataframe, primarykey_list, main_date_key):
        self.dataframe = dataframe
        self.primarykey_list = primarykey_list
        self.main_date_key = main_date_key
    
    def dupcheck(self):
        dataframe = self.dataframe
        primarykey_list = self.primarykey_list
        dup_df = dataframe.groupby(primarykey_list)
        dup_df = dup_df.filter(lambda g: len(g) > 1)
        return dup_df
    
    def nullcheck(self):
        dataframe = self.dataframe 
        null_df = dataframe.isnull().sum()
        null_df = pd.DataFrame(null_df)
        null_df.columns = ['Value']
        conditions = [(null_df['Value'] == 0) , (null_df['Value'] > 0)]
        mapped_value = ['N' , 'Y']
        null_df['Null_Ind'] = np.select(conditions ,mapped_value)
        return null_df
    
    def invalidrecords(self):
        dataframe = self.dataframe
        main_date_key = self.main_date_key
        today = date.today()
        invalid_df = self.dataframe[dataframe[self.main_date_key].dt.date > today]
        return invalid_df
    
    def basicstats(self):
        dataframe = self.dataframe
        stat = self.dataframe.describe().transpose()
        return stat
    
    #return dup_df, null_df, invalid_df, stat

def bucketing(dataframe, loan_static_date):
    '''
    function creates category for the columns required for reporting
    '''
    #LTV Category
    grouping_condition = [(sample_data['LTV'] <= 85) , ((sample_data['LTV'] > 85) & (sample_data['LTV'] <= 90)), \
                         ((sample_data['LTV'] > 90) & (sample_data['LTV'] <= 95)), (sample_data['LTV'] > 95)]
    assigned_grouping_value = ['<=85%' ,'>85% and <= 90%', '>90% and <= 95%','>95%']    
    dataframe['Loan_to_Value_Cohorts'] = np.select(grouping_condition , assigned_grouping_value)
    
    #Fico Category
    grouping_condition = [(sample_data['FICO_SCORE'] < 600) , ((sample_data['FICO_SCORE'] >= 600) & (sample_data['FICO_SCORE'] < 700)), \
                         ((sample_data['FICO_SCORE'] >= 700) & (sample_data['FICO_SCORE'] < 800)), (sample_data['FICO_SCORE'] >= 800)]
    assigned_grouping_value = ['<600' ,'600 - 699', '700 - 799','>=800']    
    dataframe['FICO_Score_Category'] = np.select(grouping_condition , assigned_grouping_value)
    
    #Loan Age Category
    org_date = loan_static_date
    org_date = dt.datetime.strptime(org_date, '%Y-%m-%d')
    org_date = org_date.date()
    sample_data['LOAN_AGE'] = (org_date - sample_data['LOAN_ORIG_DATE'].dt.date) / np.timedelta64(1, 'M')
    
    grouping_condition = [(dataframe['LOAN_AGE'].isnull()),((dataframe['LOAN_AGE'] > 0) & (dataframe['LOAN_AGE'] < 10)), ((dataframe['LOAN_AGE'] >= 10) & (dataframe['LOAN_AGE'] < 20)),\
                         ((dataframe['LOAN_AGE'] >= 20) & (dataframe['LOAN_AGE'] < 30)) , ((dataframe['LOAN_AGE'] >= 30) & (dataframe['LOAN_AGE'] < 40)),\
                         (dataframe['LOAN_AGE'] >= 40)]
    assigned_grouping_value = ['Unknown', '0-9 Months' ,'10-19 Months', '20-29 Months','30-39 Months','>=40 Months']    
    dataframe['Loan_Age_Cohorts'] = np.select(grouping_condition , assigned_grouping_value)
    
    return dataframe


def computestatistics(dataframe, groupby_list, report_attribute_name, agg_func):
    '''
    funtion produces reports based on the keys provided
    '''
    stat_df = dataframe.groupby(groupby_list).agg(agg_func)
    stat_df = stat_df[attribute_name]
    for i in agg_func:
        if i.upper() == 'COUNT':
            stat_df = stat_df.rename(columns = {i:'Loan_Count'})
        elif i.upper() == 'MEAN':
            stat_df = stat_df.rename(columns = {i : 'Average ' + str(attribute_name.capitalize())}) 
        else:
            stat_df = stat_df.rename(columns = {i : i.capitalize() + " " + str(attribute_name.capitalize())}) 
    return stat_df


def crosstab_report(dataframe, index_attr_name , colm_attr_name, report_attr_name, agg_func):
    stat_df = dataframe.pivot_table(index = index_attr_name , columns = colm_attr_name , \
                                      values = report_attr_name ,aggfunc = agg_func)
    return stat_df

def plot_graph(dataframe, bar_type, y_min , y_max, y_bucket, title, x_legend , y_legend):
    '''
    Function creates plot for the provided dataframe with 2 axis
    '''
    sns.set(rc = {'figure.figsize' : (15 , 20)})
    mp.style.use('fivethirtyeight')
    dataframe.plot(kind = bar_type)
    xnumbers = np.linspace(y_min, y_max, y_bucket)
    plt.yticks(xnumbers)
    plt.xticks(rotation = 0, horizontalalignment = "center")
    plt.title(title)
    plt.xlabel(x_legend)
    plt.ylabel(y_legend)
    plt.tight_layout()
    
    return plt


try:
    '''
    End to End Report Execution
    '''
    
    #Ensuring Exponential numbers are not printed in pandas dataframe
    pd.set_option('float_format', '{:f}'.format)
    path = os.getcwd()
    path = path.replace("\\","/")

    datalocation = "C:/Users/rahul/OneDrive/Desktop/sample_loan_data.xlsx"
    #Datalocation = datalocation.replace("\\","/")

    sample_data = pd.read_excel(datalocation)
    sample_data = sample_data[['LOAN_NUMBER' , 'LOAN_ORIG_DATE' , 'LENDER_INST_TYPE_DESCRIPTION', 'LTV','FICO_SCORE', 'CURRENT_BALANCE']]
    TS = dt.datetime.now()
    today = date.today()
    print("********************************************************************************************")
    print("\n************ Loan Segment Report Execution triggered at " + str(TS) + "***********")
    print("\n********************************************************************************************")
    # def invalidassertion():

    primarykey_list = ['LOAN_NUMBER']

    main_date_key = 'LOAN_ORIG_DATE'
    
    invoke_dataassertion = dataassertionreport(sample_data , primarykey_list, main_date_key)

    #Checking Duplicates
    print("\n*********************** DUPLICATE CHECK ***********************")
    dup_output = invoke_dataassertion.dupcheck()
    print(dup_output)

    print("\n*********************** INVALID RECORD CHECK ***********************")
    # No Originations happened which is greater than todays date. Hence, no invalid records
    invalid_output = invoke_dataassertion.invalidrecords()
    print(invalid_output)

    print("\n*********************** NULL CHECK ***********************")
    # Main Attributes Required in Reporting (Checking Null Count)
    # LOAN_NUMBER: No Null
    # LENDER_INST_TYPE_DESCRIPTION: No Null
    # CURRENT_BALANCE: No Null
    # LTV: No Null
    # LOAN_ORIG_DATE: There are null values in loan origination date that might cause issue in calculating loan Age Variable
    # FICO_SCORE:No Null
    null_output = invoke_dataassertion.nullcheck()
    print(null_output)

    print("\n*********************** BASIC STATS ON NUMERICAL ATTRIBUTES ***********************")
    #Basic Stat
    stat_df = invoke_dataassertion.basicstats()
    print(stat_df)
    
    # Create an excel file for Data Quality Report
    writer = pd.ExcelWriter(path + '/data_assertion_report_' + str(today) + '.xlsx', engine='xlsxwriter')
    dup_output.to_excel(writer, sheet_name='duplicate_check')
    null_output.to_excel(writer, sheet_name='null_check')
    invalid_output.to_excel(writer, sheet_name='invalid_data_check')
    stat_df.to_excel(writer, sheet_name='basic_stat_check')
    writer.save()
    
    #Adding Category
    loan_static_date = '2013-01-06'
    sample_data = bucketing(sample_data , loan_static_date)

    print("\n=====================>> REPORT 1 <<=====================")
    agg_func = ['count','mean','max', 'min']
    groupby_list = 'LENDER_INST_TYPE_DESCRIPTION'
    attribute_name = 'CURRENT_BALANCE'
    report1 = computestatistics(sample_data, groupby_list, attribute_name, agg_func)
    report1.to_csv(path + '/Lender_Init_Type_' + str(today) + '.csv')
    print(report1)

    print("\n=====================>> REPORT 2 <<=====================")
    agg_func = ['count','mean','max', 'min']
    groupby_list = 'Loan_to_Value_Cohorts'
    attribute_name = 'CURRENT_BALANCE'
    report2 = computestatistics(sample_data, groupby_list, attribute_name, agg_func)
    report2.to_csv(path + '/Loan_to_value_' + str(today) + '.csv')
    print(report2)

    print("\n=====================>> REPORT 3 <<=====================")
    agg_func = ['count','mean','max', 'min']
    groupby_list = 'Loan_Age_Cohorts'
    attribute_name = 'CURRENT_BALANCE'
    report3 = computestatistics(sample_data, groupby_list, attribute_name, agg_func)
    report3.to_csv(path + '/Loan_Age_Cohrot_' + str(today) + '.csv')
    print(report3)
    
    print("\n=====================>> REPORT 4 <<=====================")
    index_attr_name = 'FICO_Score_Category'
    colm_attr_name = 'Loan_to_Value_Cohorts'
    report_attr_name = 'CURRENT_BALANCE'
    agg_func = 'sum'
    report4 = crosstab_report(sample_data, index_attr_name , colm_attr_name, report_attr_name , agg_func)
    report4.to_csv(path + '/Current_UPB_' + str(today) + '.csv')
    print(report4)
    
    print("\n=====================>> BAR PLOT FOR REPORT 4 <<=====================")
    title = "CURRENT_UPB by LTV Cohorts and FICO Cohorts"
    x_legend = "FICO Score"
    y_legend = "Dollar Amount (Millions *100,000,000)"
    plt = plot_graph(report4, 'bar', 0 , 150000000, 8, title, x_legend , y_legend )

    
    #final dataframe
    sample_data.to_csv(path + '/Final_Dataframe_' + str(today) + '.csv')
    
except:
    print("\nProcess Terminated due to error......")
    print("\nProvided Error Details are as follow:")
    print(sys.exc_info[1])
