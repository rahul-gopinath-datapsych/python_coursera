import pandas as pd
import numpy as np
import datetime as dt
from datetime import date , time

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