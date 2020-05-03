import telebot
from telebot import apihelper
from telebot import types
import json


with open("Config.json", "r") as read_file:
    config = json.load(read_file)

bot = telebot.TeleBot(config['telegram-token'])

apihelper.proxy = {
    'http': config['proxy']['http'],
    'https': config['proxy']['https']
}

def keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
	btn1 = types.KeyboardButton('Глобальная статистика')
	btn2 = types.KeyboardButton('Глобальная статистика')
	btn3 = types.KeyboardButton('Глобальная статистика')
	btn4 = types.KeyboardButton('📖 Баланс')
	markup.add(btn1,btn2,btn3,btn4)
	return markup


markup = types.InlineKeyboardMarkup(row_width=2)
item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

markup.add(item1, item2)


# bot.send_message('733270620',str('nikq'));
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message)
    if message.text == 'Hello':
        bot.send_message(message.from_user.id, 'heyyyy',reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, message.text, reply_markup=keyboard())

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")


    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)
