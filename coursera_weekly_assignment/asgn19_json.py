from urllib import request , error , parse
import json

#getting input from users
#url_link= "http://py4e-data.dr-chuck.net/comments_42.xml"

url_link = "http://py4e-data.dr-chuck.net/comments_817506.json"
data = request.urlopen(url_link).read()

data = json.loads(data)
value_data = data['comments']

total_comment = 0

for i in value_data:
    total_comment = total_comment + int(i['count'])

print(total_comment)