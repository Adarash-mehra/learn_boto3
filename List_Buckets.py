import boto3
import json

session = boto3.Session()
client = session.client('s3')
response = client.list_buckets()
# name = response['Buckets']
# print(name[0]['Name'])

for i in response['Buckets']:
    print(i['Name'])