from enum import Enum
class InputType(Enum):
    inputStr = 0
    inputInt = 1

def typed(type: InputType):

    if type == InputType.inputStr:

        def str_decorator(func):
            def wrapper(n1, n2):
                s1 = str(n1)
                s2 = str(n2)
                return func(s1, s2)

            return wrapper

        return str_decorator

    if type == InputType.inputInt:

        def int_decorator(func):
            def wrapper(n1, n2, n3):
                f1 = float(n1)
                f2 = float(n2)
                f3 = float(n3)
                return func(f1, f2, f3)

            return wrapper

        return int_decorator

@typed(InputType.inputStr)
def add_two_symbols(a, b):
    return a + b

@typed(InputType.inputInt)
def add_three_symbols(a, b, с):
    return a + b + с

print(add_two_symbols("3", 5))
print(add_three_symbols(5, 0.6, "7"))
# print(add_two_symbols("a",5))
# print(add_two_symbols(5,5))
# print(add_two_symbols("a","b"))