from turtle import Turtle
import random
color = ["red","blue","green","brown","gray","purple","pink","turquoise","yellow","white","orange"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.speed('fastest')
        self.color(random.choice(color))
        self.penup()
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.refresh()

    def refresh(self):
        rand_color = random.choice(color)
        self.color(rand_color)
        new_x = random.randint(-262, 262)
        new_y = random.randint(-262, 262)
        self.goto(new_x, new_y)
