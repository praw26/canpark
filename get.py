import requests
import json

def get_sl_data(auth_token, input):

    r = requests.get('<MY_URI>', headers={'Authorization': auth_token})

    if r.status_code==200:
        print("success")
    else:
        print("error")

def main():

    auth_token = ''
    input1 = ''

    get_sl_data(auth_token, input1)
    