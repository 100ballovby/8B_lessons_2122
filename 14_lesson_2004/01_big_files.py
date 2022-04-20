with open('pi_million_digits.txt') as file:
    pi_string = ''
    for line in file:
        pi_string += line.strip()

    print(f'π = {pi_string[:50]}')
    print(len(pi_string))

    birthday = input('Введите дату рождения (ДДММГГ): ')
    if birthday in pi_string:
        print('Твоя дата рождения есть в числе π!')
    else:
        print('Твоей даты рождения нет в числе π (бот).')
