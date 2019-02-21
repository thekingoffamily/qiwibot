import telebot
import requests
import json

proxies = {
            'http' : "socks4://145.255.6.171:53177",
            'https' : "socks4://145.255.6.171:53177"
        }

api_access_token = 'be643fe09cf46af7297f94b25ecc1ace'
s = requests.Session()
s.headers['authorization'] = 'Bearer ' + api_access_token
b = s.get('https://edge.qiwi.com/funding-sources/v1/accounts/current', proxies=proxies)
info = json.loads(b.text)

def get_balance():
    i = []
    for i in info['accounts']:
        return i['balance']
    print(i)

get = get_balance()

balanc = get.get('amount')


token = '764914862:AAGfQycEKhlApnEKOsGBlkmytNbk9NzD0bE'

bot = telebot.TeleBot(token)

bot.send_message(361395559, str(balanc))
