import json
import boto3

glue = boto3.client('glue')

def lambda_handler(event, context):

    response = glue.start_job_run(JobName = "jobgluegroup7aiml")
    print("Lambda Invoke")