import json
import matplotlib.pyplot as plt

with open('salaries.json') as jf:
    result = json.loads(jf.read())

years = []
fee = []
fee_dollar = []
for year in result:  # перебираю ключи словаря
    years.append(year)
    salary = result[year]['fee']
    rate = result[year]['dollar_rate']
    sal_dol = salary / rate
    if result[year]['denominated']:
        salary = salary * 10000
    fee.append(salary / 1000)
    fee_dollar.append(sal_dol)

plt.title('Зарплаты белорусов 2002-2022')
plt.xlabel('Годы')
plt.ylabel('Сумма')
plt.grid()
plt.plot(years, fee, c='#f56342')
plt.plot(years, fee_dollar, c='#8c631b')
plt.fill_between(years, fee, fee_dollar,
                 facecolor='#f56342', alpha=0.1)
plt.xticks(years, rotation=45)  # развернуть подписи иксов на 45 градусов
plt.show()

