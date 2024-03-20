import json
from datetime import datetime
import boto3

def transform(data):
    start_date = datetime.strptime(data['startDate'], "%Y-%m-%d")
    end_date = datetime.strptime(data['endDate'], "%Y-%m-%d")
    booking_duration = (end_date - start_date).days
    data['booking_duration'] = booking_duration
    return data

def lambda_handler(event, context):
    data_tf = []
    try:
        print("Starting Transformation Process...")
        print(f"Processing {len(event['Records'])} records...")
        
        for record in event['Records']:
            record_tf = transform(record)
            data_tf.append(record_tf)

        print(f"Transformed data.")

        for record in data_tf:
            print(record)
            
        return {
            'statusCode': 200,
            'body': json.dumps('Data transformation - SUCCESSFUL!')
        }
    
    except:
        print('Data transformation - FAILED!')