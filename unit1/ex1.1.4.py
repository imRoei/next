import functools 

def add_numbers(x, y):
    return x + y

# def sum_of_digits(number):
#     return sum(map(int, str(number)))

def sum_of_digits(number):
    return functools.reduce(add_numbers,map(int,str(number)))


print(sum_of_digits(104))
