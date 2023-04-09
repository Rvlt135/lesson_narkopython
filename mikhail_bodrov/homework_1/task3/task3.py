#решение пункта 1
s1 = 'www.my_site.com#about'
s1 = s1.replace("#", "/")
print(s1)

#решение пункта 2
def add_ing(text):
    result = text.split()
    for i in range(len(result)):
        result[i] += 'ing'
    return ' '.join(result)
print(add_ing(input('введите текст для пункта 2: ')))

#решение пункта 3
s2 = "Ivanou Ivan".split()
s2.reverse()
print(*s2, end=' ')
print()

#решение пункта 4
s3 = input('введите строку для пункта 4: ')
print(s3.strip())