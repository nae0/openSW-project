import turtle as t
import math
import random

t1, t2, t3 = [None] * 3
t1x, t1y, t2x, t2y, t3x, t3y, = [0] * 6
swidth, sheight = 300, 300

if __name__ == "__main__" :
    t.setup(width = swidth + 50, height = sheight + 50)
    t.screensize(swidth, sheight)

    t1 = t.Turtle('turtle'); t1.color('red'); t1.penup()
    t2 = t.Turtle('turtle'); t2.color('green'); t2.penup()
    t3 = t.Turtle('turtle'); t3.color('blue'); t3.penup()

    t1.goto(-100, -100); t2.goto(0, 0); t3.goto(100, 100)

    while True :
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t1.left(angle); t1.forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t2.left(angle); t2.forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t3.left(angle); t3.forward(dist)

        t1x = t1.xcor(); t1y = t1.ycor()
        t2x = t2.xcor(); t2y = t2.ycor()
        t3x = t3.xcor(); t3y = t3.ycor()

        if math.sqrt(((t1x - t2x) * (t1x - t2x)) + ((t1y - t2y) * (t1y - t2y))) <= 20 or \
           math.sqrt(((t1x - t3x) * (t1x - t3x)) + ((t1y - t3y) * (t1y - t3y))) <= 20 or \
           math.sqrt(((t2x - t3x) * (t2x - t3x)) + ((t2y - t3y) * (t2y - t3y))) <= 20 :
            t1.turtlesize(3); t2.turtlesize(3);  t3.turtlesize(3)
            break

t.done()

        
