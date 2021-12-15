''' 1. Написать программу, которая находит все четные
числа от 1 до 15 и все нечетные от 35 до 80.
Записать все эти числа в разные списки.'''
even = []
odd = []

for n in range(2, 15, 2):
    even.append(n)

for n in range(35, 81, 2):
    odd.append(n)

print(even)
print(odd)


