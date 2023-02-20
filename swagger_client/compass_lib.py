import requests
from swagger_client.rest import ApiException
import swagger_client

from pprint import pprint
from typing import Any, Dict
import os
import json

import csv
#from dotenv import load_dotenv
from pathlib import Path

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Compass API
def init_conn():
    
    # New Method
    os.environ["username"] = os.environ["COMPASS_API_USERNAME"]
    os.environ['password'] = os.environ["COMPASS_API_PASS"]
    os.environ['client_id'] = os.environ["COMPASS_API_CLIENT_ID"]
    os.environ['client_secret'] = os.environ["COMPASS_API_CLIENT_SECRET"]

    # Old Method
    # creds = csv.DictReader(open(r"swagger_client\credentials.csv"),delimiter=',')

    # for cred in creds:
    #     user_creds = cred
    # os.environ['username'] = user_creds['username']
    # os.environ['password'] = user_creds['password']
    # os.environ['client_id'] = user_creds['client_id']
    # os.environ['client_secret'] = user_creds['client_secret']
    
    
   
    verify_cec_credentials_are_set()
    
    access_token =  get_one_hour_access_token()
    
    configuration =  get_api_configuration(
            access_token=access_token)
    
    user_info =  get_user_info(
            configuration=configuration)
    
    return access_token,configuration,user_info

def verify_cec_credentials_are_set():
    cec_username = os.getenv('username', None)
    cec_password = os.getenv('password', None)

    if not cec_username or not cec_password:
        raise RuntimeError(
            'Your CEC Username and Password must be set with the cec_setter tool before running ' +
            '(Usage: ". ./cec_setter.sh").')
        
def get_one_hour_access_token() -> str:
    """
    Get an access token to use the request tracker APIs
    These tokens last for one hour
    """
    response = requests.post(
        url='https://cloudsso.cisco.com/as/token.oauth2',
        params={
            'grant_type': 'password',
            'client_id': os.getenv('client_id'),
            'client_secret': os.getenv('client_secret'),
            'username': os.getenv('username'),
            'password': os.getenv('password'),
        }
    )

    assert response.status_code == 200
    access_token = response.json()['access_token']
    return access_token


def get_api_configuration(access_token: str) -> swagger_client.Configuration:
    """
    Get the API configuration based on an access token
    :param access_token: A token retrieved to use with request tracker APIs
    """
    # Configure API key authorization: bearerAuthorization
    configuration = swagger_client.Configuration()
    configuration.api_key['Authorization'] = access_token
    configuration.api_key_prefix['Authorization'] = 'Bearer'
    return configuration


def get_user_info(configuration: swagger_client.Configuration) -> Dict[str, Any]:
    """
    Get the user information based on an access token
    :param configuration: API Configuration
    """
    api_instance = swagger_client.UserInfoApi(
        swagger_client.ApiClient(configuration))

    try:
        api_response = api_instance.get_user_info()
        print("Status: " + bcolors.OKGREEN + "Connected" + bcolors.ENDC)
        return api_response
    except ApiException as e:
        print("Exception when calling UserInfoApi->get_user_info: %s\n" % e)


def create_request(configuration: swagger_client.Configuration) -> Dict[str, Any]:
    """
    Create a Compass request
    :param configuration: API Configuration
    """
    print('\n\ncreate_request')
    api_instance = swagger_client.RequestsApi(
        swagger_client.ApiClient(configuration))

    body = {
        "accountName": "Python",
        "requesterName": "requester@cisco.com",
        "requesterFunction": "BDM",
        "dealId": "12345678",
        "savId": "123456789,234567890",
        "guId": "12345678"
    }

    try:
        api_response = api_instance.create_request(body)
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling RequestsApi->create_request: %s\n" % e)


def get_request(configuration: swagger_client.Configuration, request_id: int) -> Dict[str, Any]:
    """
    Get a Compass request
    :param configuration: API Configuration
    """
    print('\n\nget_request')
    api_instance = swagger_client.RequestsApi(
        swagger_client.ApiClient(configuration))

    try:
        api_response = api_instance.get_request(request_id)
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling RequestsApi->get_request: %s\n" % e)

def get_requests2(configuration: swagger_client.Configuration,q) -> Dict[str, Any]:
    """
    Get Compass requests using a query
    :param configuration: API Configuration
    """
    api_instance = swagger_client.RequestsApi(
        swagger_client.ApiClient(configuration))
    
    try:
        api_response = api_instance.get_requests(q=json.dumps(q),max=1000,sort='requestedDtm',order='desc')
        return api_response
    except ApiException as e:
        print("Exception when calling RequestsApi->get_requests: %s\n" % e)
    
def patch_request(configuration: swagger_client.Configuration, request_id: int, body) -> Dict[str, Any]:
    """
    Update a Compass request
    :param configuration: API Configuration
    """
    api_instance = swagger_client.RequestsApi(
        swagger_client.ApiClient(configuration))

    try:
        api_response = api_instance.patch_request(body, request_id)
        return api_response 
    except ApiException as e:
        print("Exception when calling RequestsApi->patch_request: %s\n" % e)