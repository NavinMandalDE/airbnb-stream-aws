import json
import boto3

def lambda_handler(event, context):
    try:
        print('Data consumed!')
        return {
            'statusCode': 200,
            'body': json.dumps('Data consumption - SUCCESSFUL!')
        }
    except:
        print('Data consumption - FAILED!')