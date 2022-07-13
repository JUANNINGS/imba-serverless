import json
import boto3
import os

def run(event, context):
    # TODO implement
    client_glue = boto3.client('glue')
    glueJobName = os.environ["glueJobName"]
    client_glue.start_job_run(
            JobName = glueJobName,
        )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
