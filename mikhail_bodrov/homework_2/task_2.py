#1. Присвойте двум переменным любые числовые значения.
a = 8
b = 7

#2. Составьте четыре сложных логических выражения с помощью оператора and, два из которых должны давать истину, а два других - ложь.
if a > 0 and a % 2 == 0 and a < 10:
    print(True)
if a + b > 10  and a + b < 20 and (a + b) % 2 != 0:
    print(True)
if a == 8 and b == 7:
    print(False)
if a + b >= 15 and b < a:
    print(False)

#3. Аналогично выполните п. 2, но уже используя оператор or.
if a > 0 or a % 2 == 0 or a < 10:
    print(True)
if a + b > 10  or a + b < 20 or (a + b) % 2 != 0:
    print(True)
if a == 8 or b == 7:
    print(False)
if a + b >= 15 or b < a:
    print(False)

#4. Попробуйте использовать в сложных логических выражениях работу с переменными строкового типа.
s = "test"
if isinstance(s, int) == False and len(s) == 4 or s.startswith('t') and s.endswith('t'):
    print(s)