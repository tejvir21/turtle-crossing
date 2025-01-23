from turtle import Turtle

ALIGN = 'right'
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color('black')

    def level_up(self):
        self.level += 1

    def display_level(self):
        self.clear()
        self.goto(-150,260)
        self.write(arg=f"Level:{self.level}",align=ALIGN,font=FONT)