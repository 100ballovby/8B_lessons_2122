"""Не надо встраивать условие в условный цикл.
Его можно прописать в объявлении"""
x = 10

while x > 0:   # объявление
    print(x)  # тело цикла
    x -= 1  # тело цикла

