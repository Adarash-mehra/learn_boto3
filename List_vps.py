import boto3
import json


session = boto3.Session()
ec2 = session.client('ec2')

def list_vpc():
    response =ec2.describe_vpcs()
    vpcs = response.get('Vpcs', [])
    for vpc in vpcs:
        vpc_id = vpc.get('VpcId')
        vpc_id2 = vpc['VpcId']
        vpc_id3 = vpc['CidrBlockAssociationSet'][0]['AssociationId']
        for cidr in vpc['CidrBlockAssociationSet']:
            print(cidr['AssociationId'])
    print(vpc_id)
    print(vpc_id2)
    print(vpc_id3)

list_vpc()