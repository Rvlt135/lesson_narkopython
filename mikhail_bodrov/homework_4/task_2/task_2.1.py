'''1. Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:

@typed(type=’str’)
def add_two_symbols(a, b):
    return a + b

add_two_symbols("3", 5) -> "35"
add_two_symbols(5, 5) -> "55"
add_two_symbols('a', 'b') -> 'ab’

@typed(type=’int’)
def add_three_symbols(a, b, с):
    return a + b + с

add_three_symbols(5, 6, 7) -> 18
add_three_symbols("3", 5, 0) -> 8
add_three_symbols(0.1, 0.2, 0.4) -> 0.7000000000000001'''
import inspect
def typed(type_args):
    def decorator(fun):
        def wrapper(a, b, c=None):
            if type_args == 'str':
                a = str(a)
                b = str(b)
                return fun(a, b)
            elif type_args == 'int':
                if type(a) == type('') and a.isdigit() == True:
                    a = int(a)
                elif type(a) == type('') and a.isdigit() == False:
                    a = len(a)
                elif type(a) != type(0.1):
                    a = int(a)

                if type(b) == type('') and b.isdigit() == True:
                    b = int(b)
                elif type(b) == type('') and b.isdigit() == False:
                    b = len(b)
                elif type(b) != type(0.1):
                    b = int(b)

                if type(c) == type('') and c.isdigit() == True:
                    c = int(c)
                elif type(c) == type('') and c.isdigit() == False:
                    c = len(c)
                elif type(c) != type(0.1):
                    c = int(c)
                return fun(a, b, c)
        return wrapper
    return decorator

@typed(type_args='str')
def add_two_symbols(a, b):
    return a + b

@typed(type_args='int')
def add_three_symbols(a, b, с):
    return a + b + с

print(add_two_symbols(123, True))
print(add_two_symbols("test", "5"))
print(add_two_symbols(3.2, 3))
print(add_three_symbols(2, 4, 6))
print(add_three_symbols('123', True, 4))
print(add_three_symbols('test', 2, 0.123))