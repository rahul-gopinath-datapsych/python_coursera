# Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_817501.txt (There are 94 values and the sum ends with 517)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
# Data Format
# The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. Here is a sample of the output you might see:


import os
import re

#Initializig file location
dir_path=os.path.dirname(os.path.realpath(__file__))
dir_path=dir_path.replace("\\",'/')
file_name="regex_sum_817501.txt"
input_filename=dir_path+'/input_files/'+file_name

try:
    #Reading input file 
    fhandler=open(input_filename,'r')
except:
    print("Provided file name",file_name,"is not available in the path",input_filename)
    quit()

total_sum=0

# ===> Simpler Approach <===
data=fhandler.read()
input_param=re.findall('[0-9]+',data)

for num in input_param:
    print(num)
    total_sum=total_sum+int(num)

print("There are",len(input_param)," values with a sum",total_sum)

# ====> Another way of doing it <====
# for line in fhandler:
#     line=line.split()
#     for data in line:
#         input_param=re.findall('[0-9]+',data)
#         if len(input_param)>=1:
#             for num in input_param:
#                 total_sum=total_sum+int(num)
#                 count=count+1



