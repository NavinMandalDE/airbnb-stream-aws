import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')
bucket_name = 'airbnb-stream-data'
timestamp = datetime.now().strftime("%Y%m%d") #_%H%M%S
file_key = f'path/to/your/airbnb_stream_{timestamp}.json'

def lambda_handler(event, context):
    try:
        print("Starting SQS Batch Process...")
        print(f"Processing {len(event['Records'][0]['body'])} records...")
        
        for record in event['Records'][0]['body']:
            content_to_write = json.dumps(record)

        # Check if the file already exists in the bucket
        try:
            s3.head_object(Bucket=bucket_name, Key=file_key)
            file_exists = True
        except Exception as e:
            file_exists = False

        if file_exists:
            # Append to existing file
            response = s3.get_object(Bucket=bucket_name, Key=file_key)
            existing_content = response['Body'].read().decode('utf-8')
            updated_content = existing_content + '\n' + content_to_write
            s3.put_object(Bucket=bucket_name, Key=file_key, Body=updated_content.encode('utf-8'))
            print(f'Content has been appended to the existing file "{file_key}" in the S3 bucket.')
        else:
            # Write new file
            s3.put_object(Bucket=bucket_name, Key=file_key, Body=content_to_write.encode('utf-8'))
            print(f'New file "{file_key}" has been uploaded to the S3 bucket.')
            
        print('Data processed!')

        return {
            'statusCode': 200,
            'body': json.dumps('Data consumption - SUCCESSFUL!')
        }
    except Exception as err:
        print(err)
        print('Data consumption - FAILED!')

