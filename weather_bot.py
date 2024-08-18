import telebot
import requests
import json

API = '40de3915e00aed4009c42eedb839da96'

bot = telebot.TeleBot("7447457228:AAHREte9tRtittTJUMoqWmjJvjNt4fowjms")

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Напиши название города:")

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if (result.status_code == 200):
        data = json.load(res.text)
        bot.reply_to(message, f'Сейчас погода:{result.json()}')
    else:
        bot.reply_to(message, "Город указан неверно")



bot.infinity_polling()