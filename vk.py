import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import json

with open("Config.json", "r") as read_file:
    config = json.load(read_file)


keyboard = VkKeyboard(one_time=False)

keyboard.add_button('1 opt', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('2 opt', color=VkKeyboardColor.DEFAULT)

keyboard.add_line()
keyboard.add_button('3 opt', color=VkKeyboardColor.NEGATIVE)

keyboard.add_line()
keyboard.add_button('4 opt', color=VkKeyboardColor.PRIMARY)


session = requests.Session()
vk_session = vk_api.VkApi(config['vk-login'])
vk_session.auth(token_only=True)
vk_session = vk_api.VkApi(token=config['vk-token'])
longpoll = VkLongPoll(vk_session)

vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == 'Привет': #Если написали заданную фразу
            if event.from_user: #Если написали в ЛС

                vk.messages.send( #Отправляем сообщение
                    keyboard=keyboard.get_keyboard(),
                    user_id=event.user_id,
                    message='Пока',
                    random_id=get_random_id())
