import turtle




START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING = 20




class Snake:
    def __init__(self):
        self.ali_list = []
        self.creat_snake()
        self.head = self.ali_list[0]

    def creat_snake(self):
        for position in START_POSITION:
            self.add_ali(position)

    def add_ali(self,position):
        ali = turtle.Turtle("square")
        ali.color("white")
        ali.penup()
        ali.goto(position)
        self.ali_list.append(ali)

    def extend_ali(self):
        self.add_ali(self.ali_list[-1].position())

    def move(self):
        for tut in range(len(self.ali_list) - 1, 0, -1):
            new_x = self.ali_list[tut - 1].xcor()
            new_y = self.ali_list[tut - 1].ycor()
            self.ali_list[tut].goto(new_x, new_y)
        self.head.forward(MOVING)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

    def north_west(self):
        self.head.setheading(135)

    def north_East(self):
        self.head.setheading(45)

    def south_west(self):
        self.head.setheading(225)

    def south_East(self):
        self.head.setheading(315)

