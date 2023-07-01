import requests

url = 'https://jsonplaceholder.typicode.com/posts'

body = {
        "userId": "1",
        "title": "Title 111",
        "body": "Demo text 111"
}
# headers = {
#         'Content-type': 'application/json',
#         'charset': 'UTF-8',
# }

#Как оказалось работает и без хедеров
# resp = requests.post(url=url, json=body, headers=headers)

resp = requests.post(url=url, json=body)
data = resp.json()

print("Статус-код ответа:", resp.status_code)
print("Ответ с бэка с фейковым подтверждением создания новой записи", data)

# Обновление реальных данных на сервере не происходит.
# Об этом говориться на самом сайте https://jsonplaceholder.typicode.com/guide/ :
# Important: resource will not be really updated on the server but it will be faked as if.