import json


with open('series_SUGAR.json') as jf:
    rates = json.loads(jf.read())
    rates = rates['data']['rates']
    dates = []  # даты
    quantity = []  # количество сахара
    for rate in rates:
        try:
            quantity.append(rates[rate]['SUGAR'])
            dates.append(rate)
        except KeyError:  # если я обращусь к ключу, которого нет
            pass

print(quantity)
print(dates)
print(len(quantity) == len(dates))
