import boto3
import json

session = boto3.Session()
client = session.client('ec2')
response = client.describe_instances()
for i in response['Reservations']:
    for j in i['Instances']:
        print(j)