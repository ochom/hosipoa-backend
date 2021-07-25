# get Oauth token from M-pesa [function]
import base64
import logging
import datetime

import requests
from requests.auth import HTTPBasicAuth

from hosipoa import settings

logger = logging.Logger('catch_all')

BUSINESS_SHORT_CODE = settings.get_env_value('MPESA_BUSINESS_SHORT_CODE')
CONSUMER_KEY = settings.get_env_value('MPESA_CONSUMER_KEY')
CONSUMER_SECRETE = settings.get_env_value('MPESA_CONSUMER_SECRETE')
ONLINE_PASSKEY = settings.get_env_value('MPESA_ONLINE_PASSKEY')
CALLBACK_URL = settings.get_env_value('MPESA_CALLBACK_URL')


def get_mpesa_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(url, auth=HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRETE))
    return r.json()['access_token']


def sanitize_phone_number(phone):
    if phone == "":
        return phone
    if len(phone) < 11 and phone[0] == "0":
        return phone.replace("0", "254", 1)
    if len(phone) < 10 and phone[0] == "7":
        return "254" + phone
    if len(phone) == 13 and phone[0] == "+":
        return phone.replace("+", "", 1)


def push(phone, amount, order_id):
    timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')

    data = BUSINESS_SHORT_CODE + ONLINE_PASSKEY + timestamp
    encoded = base64.b64encode(data.encode())
    password = encoded.decode("utf-8")

    phone = sanitize_phone_number(phone)
    amount = int(amount)

    payload = {
        "BusinessShortCode": BUSINESS_SHORT_CODE,
        "Password": "{}".format(password),
        "Timestamp": "{}".format(timestamp),
        "TransactionType": "CustomerBuyGoodsOnline",
        "Amount": str(amount),
        "PartyA": phone,
        "PartyB": BUSINESS_SHORT_CODE,
        "PhoneNumber": phone,
        "CallBackURL": CALLBACK_URL + "?invoice=" + str(order_id),
        "AccountReference": "Hosipoa",
        "TransactionDesc": "Health Payment"
    }

    # make request and catch response
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {
        "Authorization": f"Bearer {get_mpesa_token()}",
        "Content-Type": "application/json"
    }
    response = requests.post(api_url, json=payload, headers=headers)
    print(response.json())

    if response.status_code > 299:
        return {
            "success": False,
            "payload": response.json(),
        }

    # CheckoutRequestID = response.text['CheckoutRequestID']

    # Do something in your database e.g store the transaction or as an order
    # make sure to store the CheckoutRequestID to identify the transaction in
    # your CallBackURL endpoint.

    # return a response to your user
    return {"success": True, "data": response.json()}
