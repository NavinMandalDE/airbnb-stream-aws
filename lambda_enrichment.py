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

        # Generate a timestamp for the file name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Define the output file name with timestamp
        output_file_name = f"airbnb_tf_{timestamp}.json"

        # Write the JSON list to the output file
        with open(output_file_name, "w") as output_file:
            json.dump(data_tf, output_file, indent=4)

        print(f"Transformed data has been written to {output_file_name}")

        return {
            'statusCode': 200,
            'body': json.dumps('Data transformation - SUCCESSFUL!')
        }
    
    except:
        print('Data transformation - FAILED!')