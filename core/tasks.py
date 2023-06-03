import os
from celery import shared_task
import boto3

s3 = boto3.client("s3",
                  aws_access_key_id='AKIA4DKZ67RFSA6NBM7D',
                  aws_secret_access_key='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'
                  )

dynamodb = boto3.client("dynamodb",
                  aws_access_key_id='AKIA4DKZ67RFSA6NBM7D',
                  aws_secret_access_key='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',
                  region_name='us-east-1'
                  )

@shared_task
def processFile(data):
    os.system("ccextractorwinfull "+data)

    s3.upload_file(data, "bucket-rehan-1", data)
    os.remove(data)

    filename = data.split(".")[0]

    content = open(f"{filename}.srt", "r")
    dynamodb.put_item(TableName='db1', Item={data:{'S':str(content.readlines())}, 'db1':{'S':filename}})

    # os.remove(data)