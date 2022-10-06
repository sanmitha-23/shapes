import random
import turtle
from turtle import Turtle, Screen
import colorgram

turtle.colormode(255)   # allows to randomly choose different colors


# def square(obj):
#     obj.right(90)
#     obj.forward(100)


# def dash(obj):
#     obj.pendown()
#     obj.forward(10)
#     obj.penup()
#     obj.forward(10)

# angle = 360/num of sides


# def triangle(obj):
#     for _ in range(3):
#         obj.forward(20)
#         obj.right(120)
#         obj.forward(20)
#
#
# def rectangle(obj):
#     for _ in range(4):
#         obj.forward(20)
#         obj.right(90)
#         obj.forward(20)
#
#
# def pentagon(obj):
#     for _ in range(5):
#         obj.forward(20)
#         obj.right(72)
#         obj.forward(20)
#
#
# def hexagon(obj):
#     for _ in range(6):
#         obj.forward(20)
#         obj.right(60)
#         obj.forward(20)
#
#
# def heptagon(obj):
#     for _ in range(7):
#         obj.forward(20)
#         obj.right(51.43)
#         obj.forward(20)
#
#
# def octagon(obj):
#     for _ in range(8):
#         obj.forward(20)
#         obj.right(45)
#         obj.forward(20)
#
#
# def nonagon(obj):
#     for _ in range(9):
#         obj.forward(20)
#         obj.right(40)
#         obj.forward(20)
#
#
# def decagon(obj):
#     for _ in range(10):
#         obj.forward(20)
#         obj.right(36)
#         obj.forward(20)

#  easy method

colors = ['navy', 'violet', 'dark red', 'chartreuse', 'light sky blue', 'dim gray', 'medium sea green', 'dark magenta',
          'orange', 'deep pink']
directions = [0, 90, 180, 270]




def draw_shape(sides, obj):
    angle = 360/sides
    obj.color(random.choice(colors))
    for _ in range(sides):
        obj.forward(20)
        obj.right(angle)
        obj.forward(20)


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("darkblue")

timmy_the_turtle.speed('fastest')

# triangle(timmy_the_turtle)
# rectangle(timmy_the_turtle)
# pentagon(timmy_the_turtle)
# hexagon(timmy_the_turtle)
# heptagon(timmy_the_turtle)
# octagon(timmy_the_turtle)
# nonagon(timmy_the_turtle)
# decagon(timmy_the_turtle)

for side in range(3, 11):
    draw_shape(side, timmy_the_turtle)

# this should be at end

screen = Screen()
screen.exitonclick()

