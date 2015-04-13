from turtle import *

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

    
