import telebot
import pyqiwi
from telebot import apihelper

token = '764914862:AAGfQycEKhlApnEKOsGBlkmytNbk9NzD0bE'
bot = telebot.TeleBot(token)


def balance():
    apihelper.proxy = {'http':'http://178.206.224.176:3128'}
    wallet = pyqiwi.Wallet('d25424a423bdb129db09b4c5f4ddee66', '79164763578')
    balance = wallet.balance()



@bot.message_handler(commands=['balance'])
def mes_on_start(message):
    bot.send_message(message.from_user.id, text=str(balance()))



if __name__ == '__main__':
    bot.polling(none_stop=True)
