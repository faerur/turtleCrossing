from turtle import Turtle
import car_manager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)
        self.level = 1

    def move(self):
        self.forward(10)

    def next_level(self, car):
        self.goto(STARTING_POSITION)
        car.increase_speed()
        self.level += 1

