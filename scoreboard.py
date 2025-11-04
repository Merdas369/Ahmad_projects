from turtle import Turtle
ALIGNMENT = "center"
FONT = "courier"
FONT_TYPE = "bold"
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = -1
        self.get_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score = {self.score}", False, align=ALIGNMENT,
                   font=(FONT, 15, FONT_TYPE))
    def get_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, align=ALIGNMENT,
                   font=(FONT, 15, FONT_TYPE))

