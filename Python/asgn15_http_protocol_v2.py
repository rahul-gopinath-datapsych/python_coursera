from urllib import request , error , parse

fhandle = request.urlopen("https://tarushank.github.io/tarush/")



for i in fhandle:
    print(i.decode().strip())   
