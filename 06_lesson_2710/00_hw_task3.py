a = int(input('Введите число: '))
b = int(input('Введите число: '))
summary = 0  # сумму храню здесь

for i in range(a, b + 1):  # от а до b включительно
    summary += i

print(f'Сумма чисел от {a} до {b} = {summary}')