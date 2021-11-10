name = input('Фамилия, имя, отчество, ты, ....')
summary = float(input('Сумма долга: '))
user_account = 0

while user_account < summary:
    payment = float(input(f'Ваш долг: {summary - user_account}! Сумма: '))
    user_account += payment
    if user_account < summary:
        print('Сумма недостаточна!')
    elif user_account > summary:
        print(f'Шпасиба! Вы заплатили больше! Я верну {user_account - summary} денег.')
    else:
        print('Вы погасили долг! Мы отпустим вашу семью. Наверное.')



