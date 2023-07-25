def typed(type):
    def decorator(func):
        def wrapper(*args):
            converted_args = [type(arg) for arg in args]
            result = func(*converted_args)
            return result
        return wrapper
    return decorator

@typed(type=str)
def sum_two_symbols(a, b):
    return a + b

@typed(type=int)
def sum_three_symbols(a, b, c):
    return a + b + c


