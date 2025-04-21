import json
import boto3
from datetime import date, datetime, timedelta,timezone 
import csv
from botocore.exceptions import ClientError
import os
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


def list_user(writer):

    mydict = {}
    client =  boto3.client('iam')
    response = client.list_users()
    # print(response)
    # print(response['Users'])
    for abc in response['Users']:
        # print (abc['UserName'])
        response_key = client.list_access_keys(UserName=abc['UserName'])
        # print(response_key)
        for pqr in response_key['AccessKeyMetadata']:
            # print (pqr['CreateDate'])
            today_date = datetime.now(timezone.utc)
            no_of_days = (today_date-pqr['CreateDate']).days
            # print (no_of_days)
            if(no_of_days >= 5):
                # print(abc['UserName'], pqr['AccessKeyId'], no_of_days)
                mydict['IAM_Username'] = abc['UserName']
                mydict['Access_Key'] = pqr['AccessKeyId']
                mydict['Days'] = no_of_days
                writer.writerow(mydict)
                print (mydict)

def send_email_report(file_name):
	SENDER = "veersinha07@gmail.com"
	RECIPIENT = "veersinha07@gmail.com"
	SUBJECT = "Accesskey 5 Age Data"
	ATTACHMENT = file_name
	BODY_HTML = """\
	<html>
	<head></head>
	<body>
	<h3>Hi All</h3>
	<p>Please see the attached file for a list of Accesskey those are created 100days ago.</p>
	</body>
	</html>
	"""
	CHARSET = "utf-8"
	client = boto3.client('ses')
	msg = MIMEMultipart('mixed')
	msg['Subject'] = SUBJECT 
	msg['From'] = SENDER 
	msg['To'] = RECIPIENT
	
	msg_body = MIMEMultipart('alternative')
	htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)
	msg_body.attach(htmlpart)
	att = MIMEApplication(open(ATTACHMENT, 'rb').read())
	att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))
	msg.attach(msg_body)
	msg.attach(att)
	try:
	    response = client.send_raw_email(
	        Source=SENDER,
	        Destinations=[
	            RECIPIENT
	        ],
	        RawMessage={
	            'Data':msg.as_string(),
	        }
	    ) 
	except ClientError as e:
	    print(e.response['Error']['Message'])
	else:
	    print("Email sent! Message ID:"),
	    print(response['MessageId'])



def lambda_handler(event, context):
    # TODO implement
    fieldnames = ['IAM_Username', 'Access_Key', 'Days']
    file_name = '/tmp/mydict.csv'
    with open (file_name,'w',newline='') as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writeheader()
        list_user(writer)
    send_email_report(file_name)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
