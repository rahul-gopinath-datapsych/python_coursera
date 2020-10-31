from urllib import request , error , parse
from bs4 import BeautifulSoup
import ssl

#ignoring ssl cert error
cert = ssl.create_default_context()
cert.check_hostname = False
cert.verify_mode = ssl.CERT_NONE

def read_data( link , tag ):
    '''
    funtion that retrieves data from web
    link : webpage link
    tag: anchor tag's required for particular data extraction
    '''
    cert = ssl.create_default_context()
    cert.check_hostname = False
    cert.verify_mode = ssl.CERT_NONE
    data = request.urlopen( link , context = cert).read()
    soup = BeautifulSoup( data , "html.parser")
    tags = soup(tag)
    return tags

def retrieve_info(input_list , inital_pst ,final_pst):
    '''
    function that extracts required information form the retrieved page
    input_list : output from tag's, should be a lits
    inital_pst: always set to 0
    final_pst: final position of the value to retrieve from the list
    '''
    for j in input_list:
            inital_pst = inital_pst + 1
            if inital_pst == final_pst:
                for output1 in j:
                    name = output1
                    print(name)
                url_link = j.get("href" , None)
    return url_link , name

    
#value set to None for reading inital web pge url from user
url_link = None

total_process = 7
inital_pst = 0
final_pst = 18


for i in range(0 , int(total_process)):
    if url_link is None:
        url_link = input("Enter URL: ")
        #url_link = "http://py4e-data.dr-chuck.net/known_by_Lily.html"
        tags = read_data( url_link , 'a' )
        data_list = tags[0:int(final_pst)]
        url_link , name = retrieve_info(data_list , inital_pst , final_pst)
    else:
        tags = read_data( url_link , 'a' )
        data_list = tags[0:int(final_pst)]
        inital_pst = 0
        url_link , name = retrieve_info(data_list , inital_pst , final_pst)
