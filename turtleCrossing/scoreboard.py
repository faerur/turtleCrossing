from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, level):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=-230, y=260)
        self.write(f"Level: {level.level}", align="center", font=("Courier", 20, "normal"))

    def writing(self, level):
        self.clear()
        self.write(f"Level: {level}", align="center", font=("Courier", 20, "normal"))


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Courier", 20, "normal"))