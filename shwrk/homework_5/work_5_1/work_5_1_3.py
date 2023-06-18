import requests

url = 'https://jsonplaceholder.typicode.com/posts/3'

resp = requests.get(url=url)
data = resp.json()

print("Статус-код ответа:", resp.status_code)
print("Ответ с бэка:", data)