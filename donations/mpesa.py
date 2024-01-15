import requests
import json
import base64
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

def get_mpesa_access_token():
    consumer_key = os.getenv('MPESA_CONSUMER_KEY')
    consumer_secret = os.getenv('MPESA_CONSUMER_SECRET')
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return validated_mpesa_access_token

def generate_mpesa_password():
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    business_short_code = os.getenv('MPESA_SHORTCODE')
    passkey = os.getenv('MPESA_PASSKEY')
    data_to_encode = business_short_code + passkey + lipa_time
    online_password = base64.b64encode(data_to_encode.encode())
    decoded_password = online_password.decode('utf-8')
    return decoded_password

def initiate_stk_push(phone_number, amount):
    access_token = get_mpesa_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {
        'Authorization': 'Bearer %s' % access_token,
        'Content-Type': 'application/json'
    }

    request_payload = {
        "BusinessShortCode": os.getenv('MPESA_SHORTCODE'),
        "Password": generate_mpesa_password(),
        "Timestamp": datetime.now().strftime('%Y%m%d%H%M%S'),
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": os.getenv('MPESA_PARTY_A'),
        "PartyB": 174379,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "12345678",
        "TransactionDesc": "Pay School Fees"
    }

    response = requests.post(api_url, json=request_payload, headers=headers)

    return response.text
