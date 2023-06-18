import requests

session = requests.Session()

login_url = 'https://reqres.in/api/login'
login_data = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

login_result = session.post(url=login_url, json=login_data)
login_result_json = login_result.json()

print('Статус-код ответа:', login_result.status_code)
print('json ответа:', login_result_json)

token = login_result_json['token']

print('токен ответа:', token)

# Примера хеадера токена на сайте нет.
# Запрос работает без хеадера с токеном.
# В качестве примера добавлен вымышленный хеадер с токеном.
headers = {
    'fake_token_header_key': token
}

list_url = 'https://reqres.in/api/users?page=2'
list_result = session.get(url=list_url, headers=headers)
list_result_json = list_result.json()

users = list_result_json['data']

for item in users:
    print("---------------")
    print(item['email'])
    print(item['first_name'], item['last_name'])


