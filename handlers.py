import requests
import random
import json

from voice import voice

URL = 'https://randomuser.me/api/'


def create():
    user = requests.get(URL)
    user = user.json()
    options = [
        'хорошо!',
        'подождите!'
    ]
    voice.text_to_speech(random.choice(options))
    return user


def name(user):
    name = user['results'][0]['name']
    full_name = name['title'] + name['first'] + name['last']
    voice.text_to_speech("имя пользователей: " + full_name)


def country(user):
    country = user['results'][0]['location']['country']
    voice.text_to_speech('страна' + country)


def document(user):
    with open("data_user.json",'w') as file:
        json.dump(user, file, indent=4)
    voice.text_to_speech('я уже создал анкету для пользователей')



def save(user):
    img = user['results'][0]['picture']['large']
    res = requests.get(img)

    with open("photo_user.png","wb")as file:
        file.write(res.content)

    voice.text_to_speech("я уже сохранил его фото!")
