import boto3
import json


session = boto3.Session()
ec2 = session.client('ec2')
def stop_rinstance():
    p = ec2.describe_instances()
    for runn in p['Reservations']:
        for run2 in runn['Instances']:
            if run2['State']['Name'] == 'running':
                shut=ec2.stop_instances(InstanceIds=[run2['InstanceId']])
                print(f'{run2['InstanceId']} stopping')
            else:
                print(f'{run2['InstanceId']} already stopped')
            print("-" * 100)

stop_rinstance()