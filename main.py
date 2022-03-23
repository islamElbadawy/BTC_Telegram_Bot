import requests
import time

API_KEY = "805d7e2a-1519-4324-88ee-c67f4a0b080b"
TOKEN = "5126452730:AAG6Vc20scWHI4E9MO_P67t622cn7qfTWrY"
CHAT_ID = "1100358244"

BTC_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
limit = 49000


def get_BTC_price():
    parameters = {
        'start': '1',
        'limit': '5000',
        'sort': 'name',
        'convert': 'USD',
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY,
    }
    res = requests.get(url=BTC_URL, params=parameters, headers=headers).json()["data"]
    for c in res:
        if c["name"] == "Bitcoin":
            BTC_price = c['quote']['USD']['price']

    return round(BTC_price, 2)


def send_msg(CHAT_ID, msg):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}'

    res = requests.get(url).json()
    return res


def main():
    while True:
        price = get_BTC_price()

        if price <= limit:
            msg = f'The price of The Bitcoin is ${price}'
            print(send_msg(CHAT_ID=CHAT_ID, msg=msg))
        time.sleep(5)


main()
