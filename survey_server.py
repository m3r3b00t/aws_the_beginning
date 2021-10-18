"""
Python code for survey lamda function.
"""
import json
import boto3
import datetime

def lambda_handler(event, context):

    def saveResopnses(responses):
        print("In saveResopnses")
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table('survey_tbl')
        id = str(datetime.datetime.now())
        response = table.put_item(
            Item={
                'id': id,
                'message': responses,
            }
        )
        return response
        
    if not 'responses' in event:
        return {
        'statusCode': 201,
        'body': json.dumps('Responses are not captured!')
        }
    responses = event['responses']
    print("responses are %s" %responses)
    
    res = saveResopnses(responses)
    if res['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {
            'statusCode': 200,
            'body': json.dumps('Responses are captured!')
        }
    else:
        return {
            'statusCode': 201,
            'body': json.dumps('Failed to capture responses!')
        }
