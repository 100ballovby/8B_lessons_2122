"""
Посчитать количество цифр в числе n (вводится пользователем).
СТРОКИ ИСПОЛЬЗОВАТЬ НЕЛЬЗЯ.
"""
n = int(input('Введите число: '))
c = 0
while n >= 1:
    n /= 10
    c += 1

print(c)
