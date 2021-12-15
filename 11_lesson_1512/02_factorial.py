"""
Написать программу, которая по заданному числу n считает факториал от этого числа.
Факториал - это произведение натуральных чисел от 1 до n.
"""
for n in range(11):
    factorial = 1
    for i in range(2, n + 1):
        if n == 0 or n == 1:
            factorial = 1
        else:
            factorial *= i

    print(f'{n}! = {factorial}')

