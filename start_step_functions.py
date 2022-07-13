import json
import boto3
import os


stepFunctions_client = boto3.client('stepfunctions')

region = os.environ["region"]
account_id = os.environ["account_id"]
step_functions_name = os.environ["stepfunctions_name"]

def run(event, context):
    stepFunctions_client.start_execution(
        stateMachineArn = f'arn:aws:states:{region}:{account_id}:stateMachine:{step_functions_name}',
        name = 'StepFunctions_start',
        input = json.dumps({"bucket": os.environ["data_bucket"], 
                            "prefix": os.environ["feature_prefix"],
	                        "database": os.environ["athena_database"],
	                        "query_output": f's3://{os.environ["data_bucket"]}/{os.environ["query_output"]}'})
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Step Functions is running!')
    }