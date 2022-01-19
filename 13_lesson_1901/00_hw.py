def home_work(array):
    summ = 0
    mult = 1
    for i in range(len(array)):  # повторить {длина_списка} раз
        summ += array[i]  # суммирую элементы
        mult *= array[i]  # перемножаю элементы
    mid = summ / len(array)  # среднее арифметическое (сумма на количество)
    return summ, mult, mid

print(home_work([3, 5, 6, 1, 7, 3]))


