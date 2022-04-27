import matplotlib.pyplot as plt

x = range(1, 11)  # числа от 1 до 10
y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  # квадраты
y1 = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]  # кубы

plt.title('Квадраты чисел от 1 до 10')  # подпись диаграммы
plt.xlabel('Числа')  # подпись оси X
plt.ylabel('Квадраты')  # подпись оси Y
plt.grid()  # сетку
plt.plot(x, y, c='#14ffcc', linewidth=3)  # строю диаграмму
plt.plot(x, y1, c='#147aff', linewidth=3,
         linestyle='solid',  # стиль линии графика
         marker='o',  # стиль точек на графике
         markersize=5  # толщина точек на графике
         )  # добавляю второй график на диаграмму
plt.fill_between(x, y, y1,
                 facecolor='#147aff',  # цвет заливки
                 alpha=0.3)  # прозрачность - 0.1 = 10%
plt.savefig('diagram1.jpg')  # сохранить диаграмму в файл
plt.savefig('diagram1.pdf')  # сохранить диаграмму в файл
plt.show()  # показать диаграмму
