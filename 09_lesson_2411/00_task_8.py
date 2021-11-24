"""Найти сумму элементов с четными индексами и произведение с нечетными"""

r_list = [4, 5, 12, 7, 8, 1, 9, 7, 3, 6, 20]

multiply = 1
summary = 0
for odd_index in range(1, len(r_list), 2):
    multiply *= r_list[odd_index]

for even_index in range(0, len(r_list), 2):
    summary += r_list[even_index]

print(multiply)
print(summary)