import json

with open('numbers.json') as json_file:
    data = json.loads(json_file.read())
    # .loads() преобразовывает строку в объект (массив, словарь)
    print(data[3])



