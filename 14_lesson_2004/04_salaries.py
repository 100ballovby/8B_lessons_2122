import json

with open('salaries.json') as jf:
    data = json.loads(jf.read())
    for line in data:
        fee = data[line]['fee']
        dollar_rate = data[line]['dollar_rate']
        fee_dollar = fee / dollar_rate
        print(f'Зарплата: {fee} руб,\nЗарплата в $: {fee_dollar}')