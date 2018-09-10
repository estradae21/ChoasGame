from random import randint
import turtle


def midpoint(point1, point2):
    return [(point1[0] + point2[0])/2, (point1[1] + point2[1])/2]


turns = int(input("How many turns would you like to play? "))
v1 = [-200,-100]
v2 = [0,200]
v3 = [200, -100]
current_point = [0, 200]
tut = turtle.Turtle()
tut.shape('turtle')
screen = turtle.Screen()


for _ in range(turns):
    val = randint(0, 2)
    if val == 0:
        current_point = midpoint(current_point, v1)
    if val == 1:
        current_point = midpoint(current_point, v2)
    if val == 2:
        current_point = midpoint(current_point, v3)
    tut.up()
    tut.goto(current_point[0], current_point[1])
    tut.dot(4, "black")
    tut.down()

screen.exitonclick()