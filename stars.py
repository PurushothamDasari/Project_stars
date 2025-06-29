from turtle import Turtle
import random,math

colors=['yellow','green','red','blue','purple','pink','cyan','orange']

class Stars(Turtle):
    def __init__(self):
        super().__init__()
        self.all_stars=[]
        self.shift_angle=0
        self.shrink_value =0
    def create_a_star(self):
        """creates a star at a random location"""
        new_star = Turtle()
        new_star.shape("circle")
        new_star.color("white")
        new_star.penup()
        new_star.shapesize(stretch_wid=0.05, stretch_len=0.05)
        random_x = random.randint( -750, 750)
        random_y = random.randint(-300, 300)
        new_star.goto(random_x, random_y)
        self.all_stars.append(new_star)
    def shifted_stars(self, x_coordinate, y_coordinate):
        """creates a star at the x and y coordinates given."""
        new_star = Turtle()
        new_star.shape("circle")
        new_star.color("white")
        new_star.penup()
        new_star.shapesize(stretch_wid=0.05, stretch_len=0.05)
        new_star.goto(x_coordinate, y_coordinate)
        self.all_stars.append(new_star)

    def move_stars(self):
        """using the rotational axis formulas from the coordinate systems we are able to turn the copy of points my given angle"""
        for star in self.all_stars:
            new_x = star.xcor()
            new_y = star.ycor()
            new_x_cor = math.cos(self.shift_angle) * new_x + math.sin(self.shift_angle) * new_y
            new_y_cor = math.cos(self.shift_angle) * new_y - math.sin(self.shift_angle) * new_x
            star.goto(new_x_cor,new_y_cor)

    def random_size_shifter(self,star_number,x,y):
        """randomly changes the size of the stars"""
        self.all_stars[star_number].shapesize(stretch_wid=x,stretch_len=y)

    def shrink(self):
        """shrinks the stars"""
        for star in self.all_stars:
            if star.ycor() > 0 < star.xcor():
                star.goto(star.xcor()-self.shrink_value, star.ycor()-self.shrink_value)
            elif star.ycor() > 0 > star.xcor():
                star.goto(star.xcor()+self.shrink_value, star.ycor()-self.shrink_value)
            elif star.ycor() < 0 > star.xcor():
                star.goto(star.xcor()+self.shrink_value, star.ycor()+self.shrink_value)
            else:
                star.goto(star.xcor()-self.shrink_value, star.ycor()+self.shrink_value)




