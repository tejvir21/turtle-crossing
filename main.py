import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game By Tejvir Singh Chauhan')
screen.listen()
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

#screen.onkey(key='Up',fun=player.move)
screen.onkeypress(key='Up',fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create cars.......
    cars.create_cars()

    # Cars are moving.....
    cars.move()

    # Detecting Turtle crosses all cars....
    if player.ycor() > 280:
        player.restart_player()
        scoreboard.level_up()
        cars.increase_speed()

    # Check collision with cars....
    for car in cars.segments:
       if car.distance(player) < 30:
           game_is_on = False
           cars.collision()

    scoreboard.display_level()


screen.exitonclick()