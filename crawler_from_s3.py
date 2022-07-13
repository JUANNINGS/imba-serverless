import json
import boto3
import os

glue_client = boto3.client('glue')

def run(event, context):
    glue_client.start_crawler(
        Name = os.environ["crawler_name"]
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Glue Crawler is running!')
    }