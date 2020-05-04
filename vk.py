import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import json
import data
from questions import M
from recommendation import rec
from virushack_corona import predict_corona
import random

with open("Config.json", "r") as read_file:
    config = json.load(read_file)



keyboard = VkKeyboard(one_time=False)

keyboard.add_button('Актуальные данные', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('Пройти тест', color=VkKeyboardColor.DEFAULT)
keyboard.add_line()
keyboard.add_button('Рекомендации по короновирусу', color=VkKeyboardColor.DEFAULT)


session = requests.Session()
vk_session = vk_api.VkApi(config['vk-login'])
vk_session.auth(token_only=True)
vk_session = vk_api.VkApi(token=config['vk-token'])
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

isTest = False
step = 0
progress = 0;
dataT = [[]]

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

        elif event.text == 'Рекомендации по короновирусу':
            vk.messages.send(
                keyboard=keyboard.get_keyboard(),
                user_id=event.user_id,
                message=str(rec[random.randint(0,6)]),
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
        if step > 54:
            print(dataT)
            dataT[0].append(0)
            vk.messages.send(
            user_id=event.user_id,
            message=getdata(),
            random_id=get_random_id())
            print('end')
        else:
            if event.text:
                if event.text == 'Пройти тест':
                    # continue
                    # dataT[0].append(1)
                    vk.messages.send(
                    keyboard=open('gender.json',"r",encoding="UTF-8").read(),
                    user_id=event.user_id,
                    message=str(M[step - 1]),
                    random_id=get_random_id())
                    print(dataT)

                elif progress == 0:
                    if event.text == 'Мужской':
                        dataT[0].append(1)
                        vk.messages.send(
                        user_id=event.user_id,
                        message=str(M[step - 1]),
                        random_id=get_random_id())
                        progress = progress + 1
                        print(dataT)
                    else:
                        dataT[0].append(0)
                        vk.messages.send(
                        user_id=event.user_id,
                        message=str(M[step - 1]),
                        random_id=get_random_id())
                        progress = progress + 1
                        print(dataT)
                elif progress == 1:
                    dataT[0].append(event.text)
                    vk.messages.send(
                    keyboard=open('test.json',"r",encoding="UTF-8").read(),
                    user_id=event.user_id,
                    message=str(M[step - 1]),
                    random_id=get_random_id())
                    progress = progress + 1
                    print(dataT)
                elif progress == 2:
                    if event.text == 'Да':
                        dataT[0].append(1)
                        vk.messages.send(
                        keyboard=open('test.json',"r",encoding="UTF-8").read(),
                        user_id=event.user_id,
                        message=str(M[step - 1]),
                        random_id=get_random_id())
                        print(dataT)
                    else:
                        dataT[0].append(0)
                        vk.messages.send(
                        keyboard=open('test.json',"r",encoding="UTF-8").read(),
                        user_id=event.user_id,
                        message=str(M[step - 1]),
                        random_id=get_random_id())
                        print(dataT)



                    # print(predict_corona(test))
def getdata():
    p = predict_corona(dataT)

    if int(str(p * 100)[1] + str(p * 100)[2]) > 0  :
        return str('Вероятность того, что вы зараженны короновирусом '  + str(p * 100)[1] + str(p * 100)[2] + ' %')
    else:
        return str('Вероятность того того что вы больны очень мала')
