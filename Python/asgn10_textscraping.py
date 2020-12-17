'''
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' 
like the following line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line 
(i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

File Name: mbox-short_v2.txt
'''

import os

#Initializig directory location
dir_path=os.path.dirname(os.path.realpath(__file__))
dir_path=dir_path.replace("\\",'/')
file_name="mbox-short.txt"
input_filename=dir_path+'/input_files/'+file_name

try:
    #Reading the file
    fhandler=open(input_filename,'r')
except:
    print("Provided file name",file_name,"is not available in the path",input_filename)
    quit()

#initial variable and empty list
unique_email_count=0
total_email_count=0
output_list=[]

#looping through the files to get unique email id list
for line in fhandler:
    if len(line)>3 and line.startswith("From"):
        data=line.split()
        if not data[1] in output_list:
            output_list.append(data[1])
            unique_email_count=unique_email_count+1
        total_email_count=total_email_count+1

print("Below are the",unique_email_count," unique emails in the file out of total",total_email_count,"email count")
 
for i in output_list:
    print(i)


