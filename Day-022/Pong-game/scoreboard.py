# from turtle import Turtle

# class Scoreboard(Turtle):

#     def __init__(self):
#         super().__init__()
#         self.color("white")
#         self.penup()
#         self.hideturtle()
#         self.l_score = 0
#         self.r_score = 0
#         self.update_scoreboard()

#     def update_scoreboard(self):
#         self.clear
#         self.goto(-100, 200)
#         self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
#         self.goto(100, 200)
#         self.write(self.r_score, align="center", font=("Courier", 80, "normal"))


#     def l_point(self):
#         self.l_score += 1
#         self.update_scoreboard()
    


#     def r_point(self):
#         self.r_point += 1
#         self.update_scoreboard()
        






























from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")

        self.penup()

        self.hideturtle()

        self.l_score = 0
        self.r_score = 0

        self.draw_center_line()

        self.update_scoreboard()

    def update_scoreboard(self):

        self.clear()

        self.draw_center_line()

        self.goto(-100, 200)

        self.write(
            self.l_score,
            align="center",
            font=("Courier", 80, "normal")
        )

        self.goto(100, 200)

        self.write(
            self.r_score,
            align="center",
            font=("Courier", 80, "normal")
        )

    def l_point(self):

        self.l_score += 1

        self.update_scoreboard()

    def r_point(self):

        self.r_score += 1

        self.update_scoreboard()

    def draw_center_line(self):

        self.goto(0, 300)

        self.setheading(270)

        for _ in range(15):

            self.pendown()

            self.forward(20)

            self.penup()

            self.forward(20)