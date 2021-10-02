"""Написать псевдоклон системы входа на сайт"""
login = input('Введите логин: ')  # Ctrl+D
password = input('Введите пароль: ')  # Ctrl+D
# ^ данные, которые вводит пользователь

correct_login = 'Zodiac123'  # правильные данные
correct_password = '123456qwerty'  # правильные данные

""" Как делать не надо (каскадные условия)
if (login == correct_login):
    if (password == correct_password):
        print('Добро пожаловать!') """
# проверяю введенные данные и сравниваю их с правильными
if (login == correct_login) and (password == correct_password):  # линейное условие
    print('Добро пожаловать!')
    print('flkgjfklg')
else:
    print('Доступ запрещен!')
