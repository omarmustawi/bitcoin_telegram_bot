from urllib import response
import requests
import time

# global variables
api_key = 'f622fb60-28a1-4468-882c-32365862be0c'
bot_key = '5632767930:AAFcO755gszYSSPH2qidO2sQUse_hgPfrxo'
chat_key = '1055767251'
limit = 59000
time_interval = 5 * 60



# function get the price
def get_price():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'2',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get( url , headers=headers  , params=parameters ).json()
    btc_price = response['data'][0]['quote']['USD']['price']
    return btc_price


# A function send messege if there is update
def send_update( chat_id , msg ) :
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get( url )

def main():
    while True:
        price = get_price()
        print( price )
        if price < limit:
            send_update( chat_key , f"سعر البتكوين {price}")
        time.sleep( time_interval )
main()