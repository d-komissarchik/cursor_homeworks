# 1. double_result
# This decorator function should return the result of another function multiplied by two
def double_result(func):
    def inner(a, b):
        return func(a, b) * 2

    return inner


def add(a, b):
    return a + b


print(add(5, 5))  # 10


@double_result
def add(a, b):
    return a + b


print(add(5, 5))  # 20


# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise, return the string "Please use only odd numbers!"

def only_odd_parameters(func):
    def inner(*args, **kwargs):
        for i in args:
            if i % 2 == 0:
                raise ValueError("Please use only odd numbers!")
        return func(*args, **kwargs)

    return inner


@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5))  # 10
try:
    print(add(4, 4))
except ValueError as e:
    print(e)  # Please use only odd numbers!


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


try:
    print(multiply(5, 5, 9, 11, 3))  # Must be only odd numbers
except ValueError as e:
    print(e)


# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):

def logged(func):
    def wrapper(*args, **kwargs):
        lst = []
        result = func(*args, **kwargs)
        for i in (args, kwargs):
            if len(i) != 0:
                lst.append(i)
        with open('logfile.log', 'a') as log_file:
            log_file.write(f"Result of {func.__name__} with parameters {lst} is: {result} \n")
        return result

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.

def type_check(correct_type):
    def func(func):
        def inner(num):
            if type(num) != correct_type:
                raise ValueError(f"Wrong Type: {type(num)}")
            return func(num)

        return inner

    return func


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function
