from turtle import Turtle
import time

tarta10 = Turtle()

for i in range(0,100):
    tarta10.right(90)
    tarta10.forward(100 + i*10)


# time.sleep(3)
tarta10.screen.exitonclick()