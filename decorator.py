import functools
def greet_decorator(fun):
    def wrapper():
        print("before printing")
        fun()
        print("hi")
    return wrapper

@greet_decorator
def say_hello():

    print("Hello Bro")


def log_function(w):
    def wrapper(a,b):
        print(f"Calling {functools.__name__} ")
        return a+b
    return wrapper

@log_function
def add(a, b):
    return a + b

print(add(2,3))



def my_decorator(func):
    def wrapper(*args):
        return func(*args)

    return wrapper

@my_decorator
def multiply(a, b):
    return a * b
print(multiply(4, 5))


def logger(func):
    def wrapper(*args):
        print("Calling function")
        return func(*args)
    return wrapper



@logger
def add(a, b):
    return a + b

print(add(23,25))

@logger
def multiply(a, b, c):
    return a * b * c
print(multiply(23,24,23))


def timer_message(fun):
    def wrapper():
        print("Starting function...")
        fun()
        print("Function finished!")
    return wrapper



@timer_message
def study():
    print("Studying FastAPI")
study()