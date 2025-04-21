import boto3
import json


session = boto3.Session()
client = session.client('iam')
luser = client.list_users()

print(luser['Users'][0]['UserName'])
for i in luser['Users']:
    print(i['UserId'])
    print(i['UserName'])