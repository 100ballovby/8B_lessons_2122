# Найдите произведение цифр трехзначного числа.
n = int(input('Введите трехзначное число: '))
'''
789
1. 789 / 100 = 7.89 = 7 <- целочисленное 
2. temp = 789 % 10 = 89 
3. temp // 10 = 8
4. temp % 10 = 9 
'''
hundreds = n // 100
temp = n % 100
tens = temp // 10
units = temp % 10

print(f'{hundreds} * {tens} * {units} = {hundreds * tens * units}')


