def summary(*nums):  # * позволяет ввести бесконечное количество аргументов
    res = 0
    for num in nums:  # nums превращается в список, поэтому с ним можно работать в цикле
        res += num
    return res

print(summary(3, 4, 5, 5, 6, 7))
print(summary(3, 4))
print(summary(3, 4, 6, 7, 21, 456, 1, 788, 123, 7654))