import pytest
import boto3
from botocore.exceptions import ClientError
from lambda_function import *

def test_get_table_name_with_env_var(default_table_name):
    """ Test that if TABLE_NAME is set, get_table_name returns value """
    assert get_table_name() == default_table_name
    

def test_get_table_name_with_no_env_var():
    """ Remove TABLE_NAME from env. vars if it exists, and check get_table_name fails """
    if "TABLE_NAME" in os.environ:
        os.environ.pop("TABLE_NAME")
    with pytest.raises(KeyError):
        get_table_name()


def test_ddb_table_exists(ddb_client, default_table_name, dummy_table):
    """ Check that our table exists in the mocked DDB """
    results = ddb_client.list_tables()
    assert default_table_name in results['TableNames']
    

def test_good_count_invocations(ddb_client, default_table_name, dummy_table, dummy_table_content):
    """ Check that a call to count_invocations in good env returns as expected """
    status, message = count_invocations(ddb_client, default_table_name)
    assert status == 200 and '2 times' in message
    

def test_bad_count_invocations(ddb_client, default_table_name):
    """ Check that a call to count_invocations without mocked table """
    status, message = count_invocations(ddb_client, default_table_name)
    assert status != 200 and 'ResourceNotFound' in message


def test_lambda_with_empty_event(good_context, ddb_client, default_table_name, dummy_table, dummy_table_content):
    """ Check that a standard lambda code returns 200 """
    results = lambda_handler({}, good_context)
    assert results['statusCode'] == 200 and '2 times' in results['body']
    
