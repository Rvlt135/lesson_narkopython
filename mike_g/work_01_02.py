var_int = 10
var_float = 8.4
var_str = "No"
big_int = var_int * 3.5
var_float -= 1
var_a = var_int / var_float
var_b = big_int / var_float
var_str = "No" * 2 + "Yes" * 3
print(var_int, var_float, var_str, big_int, var_a, var_b)

a = "iDwEVZPMEpU4vYCokUcknfXdZSirYqtmIEdO4HKdQOE"
char_1 = a[0]
print(char_1)
char_2 = a[-1]
print(char_2)
char_3 = a[2]
print(char_3)
last_char_3 = a[-3]
print(last_char_3)
length = len(a)
print(length)

b = "iDwEVZPMEpU4vYC"
f8_char = b[:8]
print(f8_char)
c = b[5:9]
print(c)
char_3 = b[::3]
print(char_3)
revert_char = b[::-1]
print(revert_char)

d = "my name is name"
print(d.replace('is name', 'is Mike_G'))

test_tring = "Hello world!"
i = test_tring.find("w")
print(i)
print(test_tring.count("l"))
print(test_tring.startswith("Hello"))
print(test_tring.endswith("qwe"))

test_shnyaga = "'www.my_site.com#about'"
x = test_shnyaga.replace('#', '/')
print(x)


def input_ing(syntax):
    itog = syntax.split()
    for i in range(len(itog)):
        itog[i] += 'ing'
    return ' '.join(itog)
print(input_ing(input('input text: ')))


v = "Ivanou Ivan"
v = v.split()
v.reverse()
print(*v, end=' ')


w = " Jupello, Probelli. "
print((w.lstrip()))


