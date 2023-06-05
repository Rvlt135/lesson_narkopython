'''
Задание быки и коровы обернуть в функции если вы этого не сделали, а если есть несколько функций при выполнении то оберните
хотябы в один декоратор, но желательно должна быть одна функция, а также функция декоратор как вспомогательная функция
например функция которая проверяет числа.
'''

import random

def decorator(play):
    def inner(make_riddle_number):
        riddle_number = make_riddle_number
        print('Загаданное число:', riddle_number)
        not_win = True
        while not_win:
            not_win = play(riddle_number)
    return inner

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

@decorator
def play(riddle_number):
    guess_number = make_guess_number()
    if guess_number == riddle_number:
        print('Вы выиграли!')
        return False
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
        return True


play(make_riddle_number())