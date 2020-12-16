#import pandas as pd 
import os

#Initializig directory location
dir_path=os.path.dirname(os.path.realpath(__file__))
dir_path=dir_path.replace("\\",'/')
file_name="sample_loan_data.xlsx"

print(dir_path)

# input_filename=dir_path+'/input_files/'+file_name

# sample_data = pd.read_excel("C:/Users/rahul/OneDrive/Desktop")