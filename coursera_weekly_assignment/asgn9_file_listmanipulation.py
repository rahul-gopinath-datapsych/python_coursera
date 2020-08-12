'''
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words 
using the split() method. The program should build a list of words. For each word on each line check to see 
if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.
'''

import os

#inputing file name from the user
file_name=input("Please Enter File Name: ")

#Initializig directory location
dir_path=os.path.dirname(os.path.realpath(__file__))
dir_path=dir_path.replace("\\",'/')
#file_name="romeo.txt"
input_filename=dir_path+'/'+file_name

try:
    #Reading the file
    fhandler=open(input_filename,'r')
except:
    print("Provided file name",file_name,"is not available in the path",dir_path)
    quit()

output_list=list()

for line in fhandler:
    line_list=line.split()
    for word in line_list:
        if not word in output_list:
            output_list.append(word)

output_list.sort()

print(output_list)