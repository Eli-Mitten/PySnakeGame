from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            self.save_high_score(self.score)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    @staticmethod
    def read_high_score():
        with open("data.txt") as file:
            return int(file.read())

    @staticmethod
    def save_high_score(new_end_score):
        with open("data.txt", mode="w") as file:
            file.write(f"{new_end_score}")
