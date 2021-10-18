"""
Python code for results Lambda function. 
"""

import json
import boto3

def lambda_handler(event, context):
    PWH = 0
    HW = 0
    OW = 0
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('survey_tbl')
    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    for rec in data:
        PWH += rec['message']['Permanent WFH']
        HW += rec['message']['Hybrid']
        OW += rec['message']['Office']
    return {
        'statusCode': 200,
        'body': {'Aggregate': {'PWH': PWH, 'OW': OW, 'HW': HW}, 'Responses': data}
    }
