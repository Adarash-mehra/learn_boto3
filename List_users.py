import boto3
import json
import csv


session = boto3.Session()
client = session.client('iam')
luser = client.list_users()

def list_users():
    dictt = []
    print(luser['Users'][0]['UserName'])
    for i in luser['Users']:
        dictt1 = i['UserId']
        dictt2 = i['UserName']
        dictt.append({'id': dictt1,'name': dictt2})

        return dictt
p = list_users()
with open('list_users.csv','w') as file:
    write = csv.DictWriter(file, fieldnames=['id','name'])
    write.writeheader()
    write.writerows(p)