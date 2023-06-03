import os
data = "8849331ddae9c3169024d569ce17b9a4fdd917401cd6c6bfb8dc1fd59c6af21e.srt"

import boto3

dynamodb = boto3.client("dynamodb",
                  aws_access_key_id='AKIA4DKZ67RFSA6NBM7D',
                  aws_secret_access_key='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',
                  region_name='us-east-1'
                  )

dynamodb.put_item(TableName='db1', Item={'fruitName':{'S':'Banana'}, 'db1':{'S':'db1'}})