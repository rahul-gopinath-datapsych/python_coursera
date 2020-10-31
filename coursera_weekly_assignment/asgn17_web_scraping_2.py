from urllib import request , parse , error
from bs4 import BeautifulSoup
import ssl
import regex as re

#ignoring ssl certificate errors
cert =  ssl.create_default_context()
cert.check_hostname = False
cert.verify_mode = ssl.CERT_NONE

#getting website link from user
url_link = "http://py4e-data.dr-chuck.net/comments_817503.html"
data = request.urlopen( url_link , context = cert).read()

# checking status code
status_code = request.urlopen(url_link).status
print("Request Status: " , status_code)

#initalizing Beautiful soup
soup = BeautifulSoup( data , "html.parser")

tags =  soup('span')
total_sum = 0

for i in tags:
    for j in i:
        if total_sum == 0:
            total_sum = int(j)
        else:
            total_sum = total_sum + int(j)

print("Sum: " ,total_sum)


