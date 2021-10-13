from turtle import *

t = Turtle()   # экземпляр черепашки
t.shape('turtle')  # форма черепашки
t.speed(1)  # скорость
"""
fd(x) - вперед 
bk(x) - назад
lt(g) - влево 
rt(g) - вправо
tp() - перестать рисовать 
down() - начать рисовать 
goto(x,y) - перейти в x, y 
circle(r) - круг 
"""
# квадрат
for i in range(4):
    t.fd(100)
    t.stamp()  # оставляет отпечаток черепашки
    t.rt(90)

done()  # не закрываться сразу
