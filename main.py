import telebot
import pyqiwi
from telebot import apihelper

apihelper.proxy = {'http':'74.208.83.188:80'}


token = '764914862:AAGfQycEKhlApnEKOsGBlkmytNbk9NzD0bE'
bot = telebot.TeleBot(token)

wallet = pyqiwi.Wallet(token='d25424a423bdb129db09b4c5f4ddee66', number='79164763578')



@bot.message_handler(commands=['balance'])
def mes_on_start(message):
    bot.send_message(message.from_user.id, text=str(wallet.balance()))



if __name__ == '__main__':
    bot.polling(none_stop=True)
