from turtle import Turtle
from random import random

stevenjr = Turtle()
stevenjr.pensize(10)

def random_color():
    return(random(),random(),random())

while True:
    for count in range(4):
        stevenjr.pencolor(random_color())
        stevenjr.forward(100)
        stevenjr.right(90)
    stevenjr.right(10)
    for count in range(4):
        stevenjr.pencolor(random_color())
        stevenjr.forward(160)
        stevenjr.right(90)
    
    
