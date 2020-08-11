'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, 
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of 
those values and produce an output as shown below. Do not use the sum() function or a variable named sum in 
your solution.
When you are testing below enter mbox-short.txt as the file name.
'''
import os

file_name=input("Please Enter File Name: ")

try:
    dir_path=os.path.dirname(os.path.realpath(__file__))
    file_path =dir_path.replace('\\','/') +'/'+file_name
    file_handle=open(file_path,'r')
except:
    print("Provided file name",file_path,"is not available in the path")
    quit()

#initial variable to 0
count=0
total_value=0

for line in file_handle:
    if line.startswith("X-DSPAM-Confidence:"):
        count=count+1
        line=line.strip()
        position1=line.find(":")
        input_param=line[position1+1:]
        total_value=total_value+float(input_param)

mean=total_value/count
print("Average Spam confidence:",mean)

