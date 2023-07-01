import requests

url = 'https://jsonplaceholder.typicode.com/posts'

resp = requests.get(url=url)
data = resp.json()

for item in data:
    print("---------------")
    print("Заголовок:")
    print(item["title"])
    print()
    print("Содержимое:")
    print(item["body"])
    print()
