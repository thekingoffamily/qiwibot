import telebot
import pyqiwi


token = '764914862:AAGfQycEKhlApnEKOsGBlkmytNbk9NzD0bE'
bot = telebot.TeleBot(token)





@bot.message_handler(commands=['start'])
def mes_on_start(message):
    wallet = pyqiwi.Wallet('d25424a423bdb129db09b4c5f4ddee66', '79164763578')
    balance = wallet.balance()
    bot.send_message(message.from_user.id, text=("Баланс 89164763578 сост. = ", balance))



if __name__ == '__main__':
    bot.polling(none_stop=True)
