# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. Y
# ou can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

import os

#Initializig file location
dir_path=os.path.dirname(os.path.realpath(__file__))
dir_path=dir_path.replace("\\",'/')
file_name="mbox-short.txt"
input_filename=dir_path+'/input_files/'+file_name

try:
    #Reading input file 
    fhandler=open(input_filename,'r')
except:
    print("Provided file name",file_name,"is not available in the path",dir_path)
    quit()

output_dict=dict()

for line in fhandler:
    if line.startswith('From '):
        line=line.split()
        time_data=line[5]
        final_time_data=time_data.split(':')
        hour=final_time_data[0]
        output_dict[hour]=output_dict.get(hour,0)+1

output_list=list()

#List comprehension
output_list=sorted([(key,value) for key,value in output_dict.items()])

for x,y in output_list:
    print(x,y)
