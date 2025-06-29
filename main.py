from turtle import Screen
from stars import Stars
import random

screen = Screen()
screen.setup(width=1500, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
screen.listen()

stars = Stars()
shifted_stars = Stars()
for i in range (500):
    stars.create_a_star()

for star in stars.all_stars:
    shifted_stars.shifted_stars(star.xcor(), star.ycor())

def change_shapes():
    # creating a random shapes for the stars and making a copy of it.
    for k in range(500):
        x =random.randint(1,20)*0.01
        stars.random_size_shifter(k,x,x)
        shifted_stars.random_size_shifter(k,x,x)




def turn_stars_right():
    shifted_stars.shift_angle = 0.005
    shifted_stars.move_stars()
def turn_stars_left():
    shifted_stars.shift_angle = -0.005
    shifted_stars.move_stars()
def move_up():
    for dot in shifted_stars.all_stars:
        dot.setheading(90)
        dot.forward(5)
def move_down():
    for dot in shifted_stars.all_stars:
        dot.setheading(270)
        dot.forward(5)
def shrink_key_func():
    shifted_stars.shrink_value = 5
    shifted_stars.shrink()

screen.onkeypress(turn_stars_right, "Right")
screen.onkeypress(turn_stars_left, "Left")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(shrink_key_func, "space")
screen.onkey(change_shapes, "s")




universe_alive=True
while universe_alive:
    screen.update()

screen.exitonclick()