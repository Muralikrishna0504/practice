# 1. Write a python programme to convert celsius to Fahrenheit
def celsius_to_farehnheit(celsius):
    return (celsius*(9/5))+32
print(celsius_to_farehnheit(32))

# 2. Given two inputs and swap them
def swap_numbers(a,b):
    a,b=b,a
    return a,b
print('a,b:',swap_numbers(10,20))