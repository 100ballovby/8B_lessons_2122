'''Написать программу, проверяющую високосность года:
Год делится на 4, но не делится на 100
а также Год делится на 400
'''
year = int(input('Введите год: '))
# беру значение с клавиатуры и записываю его в переменную
# функция int() преобразоывает строку из инпута в число

# оператор % возвращает остаток от деления
if ( ((year % 4) == 0) and ((year % 100) != 0) ) or ((year % 400) == 0):
    print('Високосный!')  # пишу это
else:  # иначе
    print('Не високосный!')  # пишу это
