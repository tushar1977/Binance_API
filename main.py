import binance
from binance.client import Client

API_KEY = '' #your api key
SECT_KEY = '' #your secret key


client = Client(API_KEY, SECT_KEY ,tld='com')

def get_Bal():

    info = client.get_account()
    bal = info['balances']
    for i in bal:
        if float(i['free']) > 1:
            print(i)

get_Bal()
