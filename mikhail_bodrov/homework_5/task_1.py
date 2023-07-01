'''Задание 1:
Вам необходимо написать автоматизированный скрипт, который выполняет следующие действия:

1. Отправляет GET-запрос к сервису "https://jsonplaceholder.typicode.com/posts" и получает список постов (posts).
Выведите на экран заголовок и содержимое каждого поста.

2. Затем отправляет POST-запрос на тот же сервис "https://jsonplaceholder.typicode.com/posts" с данными для создания
нового поста. Данные должны содержать заголовок и текст поста. Выведите на экран статус код ответа.

3. После создания нового поста, отправляет GET-запрос на адрес "https://jsonplaceholder.typicode.com/posts/{post_id}"
(замените {post_id} на идентификатор созданного поста). Выведите на экран заголовок и содержимое созданного поста.

4. Наконец, отправляет DELETE-запрос на адрес "https://jsonplaceholder.typicode.com/posts/{post_id}" (замените {post_id}
 на идентификатор созданного поста). Выведите на экран статус код ответа.

Подсказка:
Для выполнения авторизации в сервисе, вы можете использовать заголовки (headers) с токеном доступа или параметры запроса
 (query parameters), если сервис поддерживает такую форму авторизации.'''


import requests
import json

#1
resp1 = requests.get(url='https://jsonplaceholder.typicode.com/posts')
items = json.loads(resp1.text)
for i in items:
    print('title:', i['title'])
    print('body:', i['body'])
    print()

#2
resp2 = requests.post(url='https://jsonplaceholder.typicode.com/posts', data={'title': 'My title', 'body': 'My body'})
print(resp2.status_code)

#3
resp3 = requests.get(url='https://jsonplaceholder.typicode.com/posts/100')
item = json.loads(resp3.text)
print('title:', item['title'])
print('body:', item['body'])

#4
resp4 = requests.delete(url='https://jsonplaceholder.typicode.com/posts/100')
print(resp4.status_code)