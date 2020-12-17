'''
Parsing and extracting requried email company into the output and by removing duplicate entry
'''

email_list=["rahul.gopinath@gmail.com","tarush.k@Yahoo.com","Kiran.m@gmail.com","roha.patkar@rediff.com"]

email_company=[]

for i in email_list:
    position1=i.find("@")
    j=i[position1:]
    position2=i.find(".",position1)
    actual_data=i[position1+1:position2]
    if actual_data.upper() not in email_company:
        email_company.append(actual_data.upper())

print("Unique company email accounts are",email_company)


