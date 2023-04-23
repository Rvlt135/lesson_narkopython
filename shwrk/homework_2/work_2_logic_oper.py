a = 50
b = 100
a1 = 10
b1 = 60
print('Введите число d =')
d = int(input())
if d > a and d < b:
    print('d > 50 and d < 100')
    if d > a1 and d < b1:
        print('d > 10 and d < 60')
if d > a and d < b and d > a1 and d < b1:
    print('d находится в двух интервалах')
if d > 200 or d > 300:
    print('d > 200 или 300')