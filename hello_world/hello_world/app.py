import os

def lambda_handler(event, context):
    param = {os.environ['PARAM']}
    print(f'The version is: {param}')