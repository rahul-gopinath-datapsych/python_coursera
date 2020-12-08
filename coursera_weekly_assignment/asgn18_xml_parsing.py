from urllib import request , error , parse
import xml.etree.ElementTree as ET

#getting input from users
#url_link= "http://py4e-data.dr-chuck.net/comments_42.xml"

url_link = "http://py4e-data.dr-chuck.net/comments_817505.xml"

data = request.urlopen(url_link).read()

tree = ET.fromstring(data)
data_list = tree.findall('comments/comment')

total_comment = 0

for i in data_list:
    total_comment = total_comment + int(i.find('count').text)

print(total_comment)