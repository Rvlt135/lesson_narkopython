'''2.
BuzzFuzz
Напишите программу, которая перебирает последовательность от 1 до 100. Для чисел кратных 3 она должна написать: "Fuzz" вместо печати числа, а для чисел кратных 5  печатать "Buzz". Для чисел которые кратны 3 и 5 надо печатать "FuzzBuzz". Иначе печатать число.

Вывод должен быть следующим:
1
2
fuzz
4
buzz
fuzz
7
8'''

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FuzzBuzz')
    elif i % 3 == 0:
        print('Fuzz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)