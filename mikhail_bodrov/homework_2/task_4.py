#Перевести строку в массив
#"Robin Singh" => ["Robin”, “Singh"]
#"I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
list_1 = "Robin Singh".split()
list_2 = "I love arrays they are my favorite".split()
print(list_1)
print(list_2)

#Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
#Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
lis_3 = ['Ivan', 'Ivanou']
print(f'Привет, {lis_3[0]} {lis_3[1]}! Добро пожаловать в Minsk Belarus')

#Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него строку => "I love arrays they are my favorite"
list_4 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
s1 = ' '.join(list_4)
print(s1)

#Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
list_5 = list('клавиатура')
list_5.insert(2, "*")
list_5.pop(6)
print(list_5)