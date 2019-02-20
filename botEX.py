import telebot
from telebot import apihelper

apihelper.proxy = {'http':'74.208.83.188:80'}

token = '764914862:AAGfQycEKhlApnEKOsGBlkmytNbk9NzD0bE'

bot = telebot.TeleBot(token)

bot.send_message(361395559, "Hello")
