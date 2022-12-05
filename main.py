from random import choice
from turtle import Turtle, Screen, colormode, mode

# rgb_colors = []
# colors = color gram.extract('image.jpg', 30)

# n = 0
# for _ in colors:
#     if n < len(colors):
#         index_of_colors = colors[n]
#         coloring = index_of_colors.rgb
#         r_g_b = coloring[0], coloring[1], coloring[2]
#         n += 1
#         rgb_colors.append(r_g_b)
# print(rgb_colors)

# Alternative method / angela
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     r_g_b = (r, g, b)
#     rgb_colors.append(r_g_b)
# print(rgb_colors)

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189),
              (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16),
              (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8),
              (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239),
              (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

# All the attributes for my turtle ('speedy')
speedy = Turtle()
screen = Screen()
speedy.hideturtle()
speedy.color('blue')
speedy.speed('fastest')
speedy.setheading(225)
speedy.penup()
speedy.fd(300)
speedy.setheading(0)
screen.colormode(255)
# Current position of the turtle once all of the above lines of code were executed
start_y_axis = -162.13
start_x_axis = -212.13


def horizontal_line(box_size):
    """This function represents the horizontal line the turtle should travel"""
    for _ in range(box_size):
        speedy.dot(20, choice(color_list)), speedy.penup(), speedy.fd(50)


def vertical_line():
    """Moves the turtle vertically upwards to the next life.
    By an increment of 50 space"""
    global start_y_axis
    global start_x_axis
    speedy.setpos(start_x_axis, start_y_axis)
    start_y_axis += 50


height = 0
while height < 10:
    """ It's a 10 X 10 box, hence the reason why the loop is running 
     until the counter reaches 10."""
    horizontal_line(10)
    vertical_line()
    height += 1

screen.exitonclick()
