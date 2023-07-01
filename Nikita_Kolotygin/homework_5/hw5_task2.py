import requests
import json

# 1
Session = requests.session()

# 2
resp1 = Session.post('https://reqres.in/api/login', data={"email": "eve.holt@reqres.in", "password": "cityslicka"})
print(resp1.status_code)
print(resp1.json())
response_data = resp1.json()

#3
Session.headers = response_data
resp2 = Session.get('https://reqres.in/api/users?page=2')
user_data = json.loads(resp2.text)

for data in user_data['data']:
    print('\n Email пользователя:', data['email'])
    print('\t Имя пользователя:', data['first_name'])
    print('\t Фамилия пользователя:', data['last_name'])