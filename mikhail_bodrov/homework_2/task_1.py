#Создайте два любых списка и свяжите их с переменными.
list_1 = [i for i in range(10)]
list_2 = ['a', 'b', 'c', 'd']

#Извлеките из первого списка второй элемент.
list_1[1]

#Измените во втором списке последний элемент. Выведите список на экран.
list_2[-1]
print(list_2)

#Соедините оба списка в один, присвоив результат новой переменной. Выведите получившийся список на экран.
list_3 = list_1 + list_2
print(list_3)

#"Снимите" срез из соединенного списка так, чтобы туда попали некоторые части обоих первых списков. Срез свяжите с очередной новой переменной. Выведите значение этой переменной.
list_4 = list_3[8:12]
print(list_4)

