import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.penup()
        self.goto(x=340, y=random.randint(-250, 250))
        self.color(random.choice(COLORS))
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        self.setx(self.xcor() - self.speed)

    def detect_collision(self, player):
        if self.distance(player.xcor(), player.ycor()) < 25:
            return True

    def increase_speed(self):
        self.speed += MOVE_INCREMENT


