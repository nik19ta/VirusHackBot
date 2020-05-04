import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import json
import data
from questions import M

with open("Config.json", "r") as read_file:
    config = json.load(read_file)



keyboard = VkKeyboard(one_time=False)

keyboard.add_button('Актуальные данные', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('Пройти тест', color=VkKeyboardColor.DEFAULT)


session = requests.Session()
vk_session = vk_api.VkApi(config['vk-login'])
vk_session.auth(token_only=True)
vk_session = vk_api.VkApi(token=config['vk-token'])
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

isTest = False
step = 0

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and isTest == False:


        if event.text == 'Привет' and event.text == 'start' :
            vk.messages.send(
                keyboard=keyboard.get_keyboard(),
                user_id=event.user_id,
                message='Привет!',
                random_id=get_random_id())

        elif event.text == 'Актуальные данные':
            vk.messages.send(
                keyboard=open('k.json',"r",encoding="UTF-8").read(),
                user_id=event.user_id,
                message=data.latest(),
                random_id=get_random_id())

        elif event.text == 'Общая статистика':
            vk.messages.send(
                keyboard=open('k.json',"r",encoding="UTF-8").read(),
                user_id=event.user_id,
                message=data.latest(),
                random_id=get_random_id())

        elif event.text == 'По странам':
            vk.messages.send(
                keyboard=open('k.json',"r",encoding="UTF-8").read(),
                user_id=event.user_id,
                message=data.getLocations(),
                random_id=get_random_id())

        elif event.text == 'В главное меню':
            vk.messages.send(
                keyboard=keyboard.get_keyboard(),
                user_id=event.user_id,
                message='Главное меню:',
                random_id=get_random_id())

        elif event.text == 'Пройти тест':
            isTest = True;


        else:
            vk.messages.send(
                keyboard=keyboard.get_keyboard(),
                user_id=event.user_id,
                message='я не понимаю 😫',
                random_id=get_random_id())

    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and isTest == True:
        step = step + 1


        vk.messages.send(
            keyboard=keyboard.get_keyboard(),
            user_id=event.user_id,
            message=str(M[step - 1]),
            random_id=get_random_id())
