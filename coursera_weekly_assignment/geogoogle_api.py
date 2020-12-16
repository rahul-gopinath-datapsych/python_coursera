from urllib import parse , error , request
import json
import ssl


service_url = "http://py4e-data.dr-chuck.net/json?"

address = input("Enter the location: ")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

param = dict()
param['key'] = 42
param['address'] = address

url_details = service_url + parse.urlencode(param)

request_data = request.urlopen(url_details).read().decode()

data = json.loads(request_data)

print('Place Id: ' , data['results'][0]['place_id'])
