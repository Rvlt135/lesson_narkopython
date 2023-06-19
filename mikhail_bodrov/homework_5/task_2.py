'''Задание 2:
Используя класс Session, напишите автоматизированный скрипт, который выполняет следующие действия:

1. Создайте объект Session из библиотеки requests.

2. Отправьте POST-запрос на сервис "https://reqres.in/api/login" с данными для авторизации. Данные должны содержать
email и password. Сохраните токен доступа, полученный в ответе.

3. После успешной авторизации, отправьте GET-запрос на сервис "https://reqres.in/api/users?page=2" для получения списка
пользователей. Используйте сохраненный токен доступа в заголовке запроса.

Выведите на экран список пользователей (их имена и email) из ответа на предыдущий запрос.

Подсказка:
Используйте методы session.post() и session.get() для отправки запросов вместо обычных requests.post() и requests.get().
 Установите заголовок авторизации с помощью session.headers.'''
import json

import requests

#1
session = requests.Session()

#2
url_login = 'https://reqres.in/api/login'
data_login = {
    'email': 'eve.holt@reqres.in',
    'password': 'cityslicka'
}
login_resp = session.post(url=url_login, data=data_login)
token = json.loads(login_resp.text)
token = token['token']

#3
users_url = 'https://reqres.in/api/users?page=2'
users_headers = {
    'token': token
}
users_resp = session.get(url=users_url, headers=users_headers)
users = json.loads(users_resp.text)
for i in users['data']:
    print('name:', i['first_name'])
    print('email:', i['email'])
    print()
