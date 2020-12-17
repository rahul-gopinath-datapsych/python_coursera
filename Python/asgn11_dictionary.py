# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates 
# a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary 
# is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
#File Name: mbox-short_v2.txt


import os

#Initializig file location
dir_path=os.path.dirname(os.path.realpath(__file__))
dir_path=dir_path.replace("\\",'/')
file_name="mbox-short.txt"
input_filename=dir_path+'/input_files/'+file_name

try:
    #Reading the file
    fhandler=open(input_filename,'r')
except:
    print("Provided file name",file_name,"is not available in the path",dir_path)
    quit()


output_dict=dict()

#Counting Number of time the each email occured and saving it in for of a dictinoary
for line in fhandler:
    if line.startswith('From '):
            data_list=line.split()
            output_dict[data_list[1]]=output_dict.get(data_list[1],0)+1

#finding the maximum number of times an email occcured.
max_count=None
max_email=None

for key,value in output_dict.items():
    if max_email is None or value>max_count:
        max_email=key
        max_count=value

print(max_email,max_count)


    
