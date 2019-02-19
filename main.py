import telebot

token = '764914862:AAGfQycEKhlApnEKOsGBlkmytNbk9NzD0bE'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def mes_on_start(message):
    bot.send_message(message.from_user.id, 'Work')


if __name__ == '__main__':
    bot.polling(none_stop=True)
