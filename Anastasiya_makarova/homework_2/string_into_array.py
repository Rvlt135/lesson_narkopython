#task 1
first_string = "Robin Singh"
print(first_string.split())

second_string = "I love arrays they are my favorite"
print(second_string.split())
#task 2
lastName_fisrtName = ['Ivan', 'Ivanou']
city = "Minsk"
country = "Belarus"
print(f"Привет, {lastName_fisrtName[0]}, {lastName_fisrtName[1]}! "
      f"Добро пожаловать в {city} {country}")
#task 4
array = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(' '.join(array))
#task 5
list = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]
list.insert(2, 3)
del list[6]
print(list)