import logging
import os
import json
import random
import boto3
from botocore.exceptions import ClientError

# Set the logging level to the value specified in env. var LOG_LEVEL.
# If env. var doesn't exist, set it to INFO
logLevel = os.getenv('LOG_LEVEL', 'INFO').upper()
logger   = logging.getLogger()
logger.setLevel(logLevel)



def lambda_handler(event, context):
    return_status = 200
    return_message = "Hello world"
    choice = random.choice([1,2,3])     # We're including this to trigger a warning in bandit
    
    dynamodb = boto3.client('dynamodb', region_name ='eu-west-1')
    
    table_name = get_table_name()

    return_status, return_message = count_invocations(dynamodb, table_name)
    
    return {
        'statusCode': return_status,
        'headers': { 'Content-Type': 'text/html; charset=utf-8' },
        'body' : return_message
        }


def get_table_name():
     return os.environ['TABLE_NAME']
     

def count_invocations(ddb_client, table_name):

    try:
        # This will invoke an atomic counter on the DDB table
        res = ddb_client.update_item(
            TableName=table_name, 
            Key={'key':{'S': 'counter'}}, 
            UpdateExpression='ADD #att :inc',  
            ConditionExpression="attribute_not_exists(#a)",
            ExpressionAttributeNames={"#att": "counter", "#a": "attribute"}, 
            ExpressionAttributeValues={':inc': {'N': '1'}}, 
            ReturnValues="UPDATED_NEW"
        )
        count_value = res['Attributes']['counter']['N']
        return_message = f"API Gateway has been called {count_value} times"
        return_status = 200
    except ClientError as e:
        return_message = f"DDB Update failed - {e.response['Error']['Code']}"
        logger.error(return_message)
        return_status = 500

        
    return return_status, return_message
        


if __name__ == '__main__':
    lambda_handler({},{})