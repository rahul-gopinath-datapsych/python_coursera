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

#inputing file name from the user
file_name=input("Please Enter File Name: ")

#Initializig directory location
dir_path=os.path.dirname(os.path.realpath(__file__))
file_path =dir_path.replace('\\','/') +'/input_files/'+file_name

try:
    #Reading the file
    file_handle=open(file_path,'r')
except:
    print("Provided file name",file_name,"is not available in the path",dir_path)
    quit()

#initial variable to 0
count=0
total_value=0

for line in file_handle:
    #Checking if line exist
    if line.startswith("X-DSPAM-Confidence:"):
        #Slicing for the numeric value
        count=count+1
        line=line.strip()
        position1=line.find(":")
        input_param=line[position1+1:]
        #Converting and adding numeric variable
        total_value=total_value+float(input_param)

#Calculating Average
mean=total_value/count
print("Average Spam confidence:",mean)

