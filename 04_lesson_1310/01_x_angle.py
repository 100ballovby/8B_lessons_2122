from turtle import *

t = Turtle()   # экземпляр черепашки
t.shape('turtle')  # форма черепашки

angle = int(input('Количество сторон: '))

for i in range(angle):
    t.fd(0.1)
    t.rt(360 / angle)
    t.write(360 / angle)

done()
