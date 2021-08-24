def logger(func):
    def wrapper(*args, **kwargs):
        str = ""
        for i in args:
            str += f'{args}'
        for k in kwargs:
            str += f'{kwargs[k]}'
            print(f'Executing of function {func.__name__} with arguments {str[2:]}...')
            return func(*args, **kwargs)
        return wrapper

def concat ():
    pass

@logger
def sum(a, b):
    return a + b


@logger
def print_arg(arg):
    print(arg)
