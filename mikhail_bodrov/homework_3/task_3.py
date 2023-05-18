'''3.
Быки и коровы
В классическом варианте игра рассчитана на двух игроков. Каждый из игроков задумывает и записывает тайное 4-значное число с неповторяющимися цифрами. Игрок, который начинает игру по жребию, делает первую попытку отгадать число. Попытка — это 4-значное число с неповторяющимися цифрами, сообщаемое противнику. Противник сообщает в ответ, сколько цифр угадано без совпадения с их позициями в тайном числе (то есть количество коров) и сколько угадано вплоть до позиции в тайном числе (то есть количество быков).
При игре против компьютера игрок вводит комбинации одну за другой, пока не отгадает всю последовательность.
Ваша задача реализовать программу, против которой можно сыграть в "Быки и коровы"
Пример
Загадано число 3219
     2310
Две коровы, один бык
     3219
Вы выиграли!'''

import random

def make_riddle_number():
    riddle_number = set()
    while len(riddle_number) < 4:
        riddle_number.add(random.randrange(0, 9))
    return list(riddle_number)

def make_guess_number():
    guess_number_not_valid = True
    while guess_number_not_valid:
        guess_number = []
        for i in input('Введите четырехзначеное число с неповторяющимися цифрами: '):
            if i.isdigit() == False:
                    break
            else:
                guess_number.append(int(i))
        if len(set(guess_number)) == 4:
            guess_number_not_valid = False
        else:
            print('Введенное значение должно быть четырехзначным числом, состоящее из неповторяющихся чисел без пробелов, букв и спецсимволов')
    return guess_number


riddle_number = make_riddle_number()
print('Загаданное число:', riddle_number)
not_win = True
while not_win:
    guess_number = make_guess_number()
    if guess_number == riddle_number:
        print('Вы выиграли!')
        not_win = False
    else:
        cow_count = 0
        bull_count = 0
        for i in range(len(guess_number)):
            for j in range(len(guess_number)):
                if guess_number[i] == riddle_number[j] and i != j:
                    cow_count += 1
                elif guess_number[i] == riddle_number[j] and i == j:
                    bull_count += 1
                else:
                    continue
        print('Количество коров:', cow_count)
        print('Количество быков:', bull_count)
