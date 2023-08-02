from .db_handler import insert_data
from .sqs_handler import read_from_sqs
from .masker import mask_pii
import json

def run_etl():
    messages = read_from_sqs()
    for message in messages['Messages']:
        if 'Body' in message.keys():
            body=json.loads(message['Body'])
            print(type(body))
            masked_data = mask_pii(body)
            insert_data(masked_data)

if __name__ == '__main__':
    run_etl()