'''Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ заменяется другим, отстоящим от него в алфавите
 на фиксированное число позиций.
Примеры:
hello world! -> khoor zruog!
this is a test string -> ymnx nx f yjxy xywnsl'''

text = input('Введите текст для шифрования: ')
n = input('Введите шаг шифрования:')
words = text.split()
result = ""

for i in words:
    leters = list(i)
    #отбираем спецсимволы и записываем их в результирующую строку без шифрования, при этом добавляя пробел после них, если они стоят в конце слова
    for j in range(len(leters)):
        if leters[j].isalpha() == False and j != len(leters) - 1:
            result += leters[j]
        elif leters[j].isalpha() == False and j == len(leters) - 1:
            result += leters[j] + " "
        else:
            #шифруем буквы и записываем в результирующую строку, при этом добавляя пробел после буквы, если она расположена в конце слова
            if ord(leters[j]) >= 97 and ord(leters[j]) <= 122:
                if ord(leters[j]) + n <= 122:
                    result += chr(ord(leters[j]) + n)
                    if j == len(leters) - 1:
                        result += " "
                else:
                    result += chr(ord(leters[j]) + n - 122 + 97 - 1)
                    if j == len(leters) - 1:
                        result += " "
# убираем лишний пробел в конце результирующей строки
result = result.rstrip()

print(result)
