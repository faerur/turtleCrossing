import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
cars = [CarManager()]

player = Player()
score = Scoreboard(player)

game_is_on = True
i = 0
while game_is_on:
    time.sleep(0.1)

    screen.update()
    screen.listen()
    screen.onkey(key="Up", fun=player.move)
    for car in cars:
        car.move()
        if car.detect_collision(player):
            score.game_over()
            game_is_on = False
        for element in cars:
            if player.ycor() >= 280:
                player.next_level(element)
                score.writing(player.level)
    if i % 6 == 0:
        cars.append(CarManager())


    i += 1





screen.exitonclick()
