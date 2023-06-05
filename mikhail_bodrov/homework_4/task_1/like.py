'''
Задание с лайками обернуть в функции если вы этого не сделали, а если есть несколько функций при выполнении то оберните
хотябы в один декоратор, но желательно должна быть одна функция, а также функция декоратор как вспомогательная функция
например функция которая проверяет числа.
'''

def decorator(fun):
    def inner(lst):
        print(fun(lst))
        print("Общее количество лайков:", len(lst))
    return inner


@decorator
def likes(names_list):
    if type(names_list) != type([]):
        return 'Неверный тип данных'
    if len(names_list) == 0:
        return 'no one likes this'
    cyrillic = False
    latin = False
    other_cymbol = False
    for i in names_list:
        for j in i:
            if ord(j) >= 1040 and ord(j) <= 1103 or ord(j) == 1105 or ord(j) == 1025:
                cyrillic = True
            elif ord(j) >= 65 and ord(j) <= 90 or ord(j) >= 97 and ord(j) <= 122:
                latin = True
            else:
                other_cymbol = True
    if other_cymbol == True:
        return 'Имена должны состоять только из букв алфавита'
    if latin == True and cyrillic == True:
        return 'Имена должны состоять только из кириллических символов или только из латинских символов'
    if latin == True and cyrillic == False:
        if len(names_list) == 1:
            return f'{names_list[0]} likes this'
        elif len(names_list) == 2:
            return f'{names_list[0]} and {names_list[1]} likes this'
        elif len(names_list) == 3:
            return f'{names_list[0]}, {names_list[1]} and {names_list[2]} likes this'
        elif len(names_list) > 3:
            return f'{names_list[0]}, {names_list[1]} and {len(names_list) - 2} others likes this'
    if latin == False and cyrillic == True:
        if len(names_list) == 1:
            return f'{names_list[0]} нравится это'
        elif len(names_list) == 2:
            return f'{names_list[0]} и {names_list[1]} нравится это'
        elif len(names_list) == 3:
            return f'{names_list[0]}, {names_list[1]} и {names_list[2]} нравится это'
        elif len(names_list) > 3:
            return f'{names_list[0]}, {names_list[1]} и {len(names_list) - 2} другим нравится это'


names = input('введите имена через пробел: ').split()
likes(names)
