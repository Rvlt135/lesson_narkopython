import requests

#1
resp = requests.get('https://jsonplaceholder.typicode.com/posts')
print(resp.headers)
print(resp.text) #в юникоде
print(resp.json()) #в json

#2
resp2 = requests.post('https://jsonplaceholder.typicode.com/posts', data = {'title':'Мой заголовок', 'body': 'Мне этот мир абсолютно понятен'})
print(resp2.status_code)
print(resp2.text)

#3
resp3 = requests.get('https://jsonplaceholder.typicode.com/posts/100')
print(resp.headers)
print(resp3.text)

#4
resp4 = requests.delete('https://jsonplaceholder.typicode.com/posts/100')
print(resp4.status_code)
print(resp4.text)
