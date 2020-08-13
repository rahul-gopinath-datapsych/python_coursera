'''
7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
and print the contents of the file in upper case. Use the file words.txt to produce the output below.
'''

import os

file_name=input("Please Enter File Name: ")

try:
    dir_path=os.path.dirname(os.path.realpath(__file__))
    file_path =dir_path.replace('\\','/') +'/input_files/'+file_name
    file_handle=open(file_path,'r')
except:
    print("Provided file name",file_name,"is not available in the path")
    quit()

for line in file_handle:
    print(line.upper().rstrip())
