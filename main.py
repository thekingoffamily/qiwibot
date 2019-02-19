import telebot
import pyqiwi

token_qiwi = 'd25424a423bdb129db09b4c5f4ddee66'
number_qiwi = '79164763578'

token = '764914862:AAGfQycEKhlApnEKOsGBlkmytNbk9NzD0bE'
bot = telebot.TeleBot(token)




@bot.message_handler(commands=['start'])
def mes_on_start(message, token_qiwi, number_qiwi):
    wallet = pyqiwi.Wallet(token=token_qiwi, number=number_qiwi)
    balance = wallet.balance()
    bot.send_message(message.from_user.id, balance)



if __name__ == '__main__':
    bot.polling(none_stop=True)
