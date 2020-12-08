import xml.etree.ElementTree as ET
import os

#Initializig file location
dir_path=os.path.dirname(os.path.realpath(__file__))
dir_path=dir_path.replace("\\",'/')
#XML file
file_name="person.xsd"
input_filename=dir_path+'/input_files/'+file_name

try:
    #Reading the file
    fhandler=open(input_filename,'r')
except:
    print("Provided file name",file_name,"is not available in the path",dir_path)
    quit()


tree = ET.fromstring(fhandler.read())
#creates an iterative list
data_list = tree.findall('people/user')

for i in data_list:
    print("******* MEMBER DETAILS *******")
    print('Membership ID: ', i.find('name').get('member_id'))
    print('Name: ' , i.find('name').text)
    print('phone: ' , i.find('phone').text)
    print('sex: ' , i.find('sex').text)

