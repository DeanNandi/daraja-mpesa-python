# mpesaapi/accessToken.py
import requests
from requests.auth import HTTPBasicAuth

def get_mpesa_access_token():
    consumer_key = "SlGJBVl3sM7rSsXwZLkh1FfAp4GIDzqx"
    consumer_secret = "GOemztpKjbpcdzQA"
    access_token_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    auth = HTTPBasicAuth(consumer_key, consumer_secret)
    response = requests.get(access_token_url, auth=auth, headers={'Content-Type': 'application/json; charset=utf8'})

    if response.status_code == 200:
        result = response.json()
        access_token = result['access_token']
        return access_token
    else:
        print(f"Failed to obtain access token. Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")
        return None
