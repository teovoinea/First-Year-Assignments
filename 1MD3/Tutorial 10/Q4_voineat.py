from turtle import *
from random import *

Screen()
def tree(length, angle, factor, degree):
    if degree > 0: 
        degree = degree - 1       
        left(angle)
        forward(length*factor)
        #print(degree)
        tree(length * factor, angle, factor, degree)
        backward(length*factor)
        right(angle * 2)
        forward(length*factor)
        #print(degree)
        tree(length * factor, angle, factor, degree)
        backward(length*factor)
        left(angle)

    
def forest():
    left(90)
    length = 100
    angle = 7
    factor = 0.7
    degree = 0
    for i in range(10):
        degree = randint(4,7)
        penup()
        setpos(randint(-100,100), randint(-100,100))
        pendown()
        tree(length, angle, factor, degree)
