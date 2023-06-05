def typed(function_to_decorate):
    def wrapper_func(*args, **kwargs):
        function_to_decorate(*args, **kwargs)
    return wrapper_func

@typed
def add_two_symbols(a,b):
    print("Sum of string elements =", str(a)+str(b))

print("Введите значение А:")
a = input()
print("Введите значение Б:")
b = input()
add_two_symbols(a,b)

@typed
def add_three_symbols(c,d,e):
    if (type(c) == float or type(d) == float or type(e) == float):
        print("Sum of int elements =", c + d + e)
    else:
        print("Sum of int elements =", int(c) + int(d) + int(e))
    # print("Type c", type(c), "Type d", type(d), "Type e", type(e))

add_three_symbols(1,"3",3)
add_three_symbols(0.1,0.8,3)