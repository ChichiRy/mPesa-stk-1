import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64


import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64


class Credentials:
    consumer_key = '4kGLtsCFg4fQVHoyVrVdKhsG248VOnNg'
    consumer_secret = 'oarn7VV9NkBN4mMG'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    t = requests.get(Credentials.api_URL,
                     auth=HTTPBasicAuth(Credentials.consumer_key,  Credentials.consumer_secret))
    access_token = json.loads(t.text)
    validated_access_token = access_token["access_token"]


class MpesaPpassword:
    pay_time = datetime.now().strftime('%Y%m%d%H%M%S')
    short_code = "174379"
    OffSetValue = '0'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    encode = short_code + passkey + pay_time

    encoded = base64.b64encode(encode.encode())
    decoded = encoded.decode('utf-8')



# class Credentials:
#     consumer_key = '4kGLtsCFg4fQVHoyVrVdKhsG248VOnNg'
#     secret_key = 'oarn7VV9NkBN4mMG'
#     pass_key = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
#     api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credential'
#
#
# class MpesaAccessToken:
#     request = requests.get(Credentials.api_url, auth=HTTPBasicAuth(Credentials.secret_key, Credentials.consumer_key))
#     access_token = json.loads(request.text)
#     validated_access_token = access_token['access_token']
#
#
# class MpesaPpassword:
#     pay_time = datetime.now().strftime('%Y%m%d%H%M%S')
#     shortcode = '174379'
#     OffSetValue = '0'
#     passkey = Credentials.pass_key
#
#     encoded_data = shortcode + passkey + pay_time
#
#     mpesa_password = base64.b64encode(encoded_data.encode())
#     decoded_password = mpesa_password.decode('utf-8')
