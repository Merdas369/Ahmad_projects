from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
            self.timy_group = []
            self.snake_create()
            self.head = self.timy_group[0]

    def snake_create(self):
        for i in START_POS:
            self.add_snake(i)

    def add_snake(self, position):
            timy = Turtle(shape="square")
            timy.color("white")
            timy.penup()
            timy.goto(position)
            self.timy_group.append(timy)

    def extend(self):
        self.add_snake(self.timy_group[-1].pos())

    def move(self):
        for timy in range(len(self.timy_group) - 1, 0, -1):
            new_pos = self.timy_group[timy - 1].pos()
            self.timy_group[timy].goto(new_pos)
        self.timy_group[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)