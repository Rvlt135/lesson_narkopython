from math import floor

#решение пункта 1
s1 = 'абракадабра'
print('Первый символ строки "s1":', s1[0])
print('Последний символ строки "s1":', s1[-1])
print('Третий символ с начала строки "s1":', s1[2])
print('Третий символ с конца строки "s1":', s1[-3])
print('Длина строки "s1":', len(s1))

#решение пункта 2
s2 = 'асимметричность'
print('Первые восемь символов строки "s2"', s2[:8])
print('Четыре символа из центра строки "s2"', s2[floor(len(s2) / 2) - 2:floor(len(s2) / 2) + 2])
def multiple_of_index_3(text):
    result = ''
    for i in range(len(text)):
        if i != 0 and i % 3 == 0:
            result += text[i]
    return result
print('Cимволы строки "s2" с индексами кратными 3:', multiple_of_index_3(s2))
print('Перевернутая строка "s2":', s2[::-1])

#решение пункта 3
s3 = 'my name is name'
print(s3.replace('is name', 'is Mikhail'))

#решение пункта 4
test_sring = "Hello world!"
print(f'В строке "{test_sring}" буква "w" находится на {test_sring.index("w") + 1}-м месте')
if test_sring.startswith('Hello'):
    print(f'Строка "{test_sring}" начинается с подствроки "Hello"')
else:
    print(f'Строка "{test_sring}" не начинается с подствроки "Hello"')
if test_sring.endswith('qwe'):
    print(f'Строка "{test_sring}" заканчивается подстврокой "qwe"')
else:
    print(f'Строка "{test_sring}" не заканчивается подстврокой "qwe"')