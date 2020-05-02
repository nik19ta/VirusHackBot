import telebot
from telebot import apihelper
import json


with open("Config.json", "r") as read_file:
    config = json.load(read_file)

bot = telebot.TeleBot(config['telegram-token'])

apihelper.proxy = {
    'http': config['proxy']['http'],
    'https': config['proxy']['https']
}


# bot.send_message('733270620',str('nikq'));
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        print(message)
        bot.send_message(message.from_user.id, "Нуууу, я не буду говорить что ты болен, но лучше сиди дома")

bot.polling(none_stop=True)
