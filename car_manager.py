from turtle import Turtle
import random as rd

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
ALIGN = 'center'
FONT = ("Courier", 24, "bold")

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.start_speed = STARTING_MOVE_DISTANCE
        self.speed_increment = MOVE_INCREMENT
        self.segments = []
    def create_cars(self):
        random_chance = rd.randint(1,6)
        if random_chance == 1:
            car = Turtle('square')
            car.color(rd.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            # x = rd.randrange(-300, 300)
            y = rd.randint(-250, 250)
            car.goto(300, y)
            self.segments.append(car)

    def move(self):
        for i in self.segments:
           i.backward(self.start_speed)

    def increase_speed(self):
        self.start_speed += self.speed_increment

    def collision(self):
        self.pencolor('black')
        self.write(arg='GAME OVER',align=ALIGN,font=FONT)
