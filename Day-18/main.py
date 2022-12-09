# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
color_list = [(224, 158, 77), (37, 109, 152), (118, 163, 192), (154, 61, 85), (181, 160, 33), (207, 132, 157), (27, 133, 96), (216, 86, 58), (119, 180, 150), (200, 84, 111), (165, 79, 48), (142, 32, 41), (214, 227, 217), (54, 167, 135), (6, 107, 83), (233, 197, 103), (229, 209, 219), (42, 160, 185), (202, 217, 224), (117, 114, 163), (236, 161, 180), (31, 62, 112), (239, 168, 154), (125, 38, 36), (154, 210, 199), (33, 57, 80), (69, 42, 40), (25, 65, 58), (76, 36, 45)]

tim.speed("fast")

tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()


