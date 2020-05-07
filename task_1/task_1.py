import requests
import json

def loginbot(login, password):
    session = requests.Session()
    session.get("https://goodgame.ru/forum")

    data = {"backurl":'',
            'login':login,
            'password':password,
            'remember':	'1',
            'return': 'user'
    }

    request = session.post("https://goodgame.ru/ajax/login/", data = data)
    print(request.text)

loginbot(input("Input login: "), input("Intput password: "))
