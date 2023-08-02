import boto3
from .config import SQS_URL

def get_sqs_client():
    sqs = boto3.client('sqs', endpoint_url=SQS_URL)
    return sqs

def read_from_sqs():
    sqs = get_sqs_client()
    messages = sqs.receive_message(QueueUrl=SQS_URL)
    return messages
