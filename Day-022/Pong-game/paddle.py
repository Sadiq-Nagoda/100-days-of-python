# from turtle import Turtle, Screen


# class Paddle(Turtle):

#     def __init__(self, position):
#         super().__init__()
#         self.shape("square")
#         self.color("white")
#         self.shapesize(stretch_wid=5, stretch_len=1)
#         self.penup()
#         self.goto(position)


#     def move_up(self):
#         new_y = self.ycor() + 20
#         self.goto(self.xcor(), new_y)

#     def move_down(self):
#         new_y = self.ycor() - 20
#         self.goto(self.xcor(), new_y)
























from turtle import Turtle

MOVE_DISTANCE = 20
UP = 20
DOWN = -20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")

        self.shapesize(stretch_wid=5, stretch_len=1)

        self.penup()

        self.goto(position)

    def move_up(self):

        if self.ycor() < 250:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def move_down(self):

        if self.ycor() > -250:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)