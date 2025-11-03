from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.scoreboard_update()

    
    def scoreboard_update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def the_game_is_over(self):
        self.goto(0, 0)
        self.write("The Game is Over", align=ALIGNMENT, font=FONT)


    def score_up(self):
        self.score += 1
        self.clear()
        self.scoreboard_update()