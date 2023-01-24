import os
import pytest
import boto3
from moto import mock_dynamodb


# Create example lambda context for invoking lambda calls
class lambda_context(object):
    def __init__(self, invokeid, context_objs = None, client_content = None, invoked_function_arn = None):
        self.aws_request_id = invokeid
        self.invoked_function_arn = invoked_function_arn
        self.identity = None
        

# Setup default logging level to be ERROR
@pytest.fixture(autouse=True)
def default_log_level():
    os.environ['LOG_LEVEL'] = 'ERROR'
    yield


# Setup TABLE_NAME environment variable
@pytest.fixture
def default_table_name():
    return 'gatewayCounter'
    

@pytest.fixture(autouse = True)
def set_table_name_env_var(default_table_name):
    os.environ['TABLE_NAME'] = default_table_name
    yield


# Setup context for testing lambda calls
@pytest.fixture
def good_context():
    return lambda_context(
        invokeid='27db2a30-973e-1234-beeb-1c49a27ac257',
        invoked_function_arn = 'arn:aws:lambda:eu-west-1:1234567890:function:test_lambda'
    )
    

# Mock AWS Credentials
@pytest.fixture()
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


# Setup a mocked boto3 ddb_client    
@pytest.fixture
def ddb_client(aws_credentials):
    with mock_dynamodb():
        conn = boto3.client("dynamodb", region_name="eu-west-1")
        yield conn
        

# Create a mocked ddb table       
@pytest.fixture
def dummy_table(aws_credentials, ddb_client, default_table_name):
    ddb_client.create_table(
        TableName=default_table_name,
        AttributeDefinitions=[
            {"AttributeName": "key", "AttributeType": "S"}
        ],
        KeySchema=[
            {"AttributeName": "key", "KeyType": "HASH"}
        ],
        BillingMode="PAY_PER_REQUEST"
    )

    yield
    
# Add content to mocked table
@pytest.fixture
def dummy_table_content(aws_credentials, ddb_client, dummy_table, default_table_name):
    ddb_client.put_item(
        TableName = default_table_name,
        Item = {
            'key': {'S':'counter'},
            'counter': {'N':'1'}}
    )

    yield

    