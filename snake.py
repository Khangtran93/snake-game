from turtle import Turtle
import random

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

color = ["red","blue","green","brown","gray","purple","pink","turquoise","yellow","white","orange"]

class Snake:

    def __init__(self):
        self.speed = 0.3
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.create_segment(position, random.choice(color))

    def create_segment(self, position, f_color):
        new_segment = Turtle('square')
        new_segment.color(f_color)

        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = (self.segment[seg_num-1]).xcor()
            new_y = (self.segment[seg_num - 1]).ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        print(self.segment[0].position())

    def extend(self, f_color):
        self.create_segment(self.segment[-1].position(), f_color)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def to_og(self):
        self.head.goto(STARTING_POSITION[0])

    def increase_speed(self):
        if self.speed > 0.1:
            self.speed -= 0.01
    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]
        self.speed = 0.3