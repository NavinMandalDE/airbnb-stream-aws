import json
import boto3

def process_data(data):
    print(data)

def lambda_handler(event, context):
    try:
        print("Starting SQS Batch Process...")
        print(f"Processing {len(event['Records'])} records...")
        
        for record in event['Records']:
            process_data(record)

        print('Data processed!')

        return {
            'statusCode': 200,
            'body': json.dumps('Data consumption - SUCCESSFUL!')
        }
    
    except:
        print('Data consumption - FAILED!')