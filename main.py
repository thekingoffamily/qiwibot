import telebot
import pyqiwi as q

wallet = q.Wallet(token='d25424a423bdb129db09b4c5f4ddee66', number='79164763578')
balance = str(wallet.balance())
token = '764914862:AAGfQycEKhlApnEKOsGBlkmytNbk9NzD0bE'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def mes_on_start(message):
    bot.send_message(message.from_user.id, 'Work')

@bot.message_handler(commands=['bal1'])
def mes_on_start(message):
    wallet = pyqiwi.Wallet(token='d25424a423bdb129db09b4c5f4ddee66', number='79164763578')
    bot.send_message(message.from_user.id, wallet.balance())

@bot.message_handler(commands=['test'])
def balance1(message):
    global balance
    bot.send_message(message.from_user.id, balance)


if __name__ == '__main__':
    bot.polling(none_stop=True)
