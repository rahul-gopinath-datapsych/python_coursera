from urllib import request , error , parse
from bs4 import BeautifulSoup
import ssl

#Sample URL : http://py4e-data.dr-chuck.net/known_by_Lily.html

#getting input from users
url_link = input("Enter URL: ")
total_process = int(input("Enter total process count: "))
final_pst = int(input("Enter total loop per count: "))


for i in range( 0 , total_process):
    data = request.urlopen( url_link).read()
    soup = BeautifulSoup( data , "html.parser")
    tags = soup('a')
    data_list = tags[int(final_pst) - 1]
    for name in data_list:
        print(name)
    url_link = data_list.get('href' , None)
        
    
