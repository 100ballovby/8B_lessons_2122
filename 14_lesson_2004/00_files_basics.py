with open('pi_digits.txt') as file_object:
    # открывает файл и присваивает его переменной file_object
    pi_string = ''
    for line in file_object:  # сохраняю содержимое файла в переменной
        pi_string += line.strip()  # убираю лишние пробелы по краям строки
    print(pi_string)
    print(f'Тип данных: {type(pi_string)}')

# print(file_object.read()) <- будет ошибка, потому что файл уже закрыт
