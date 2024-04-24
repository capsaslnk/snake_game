from turtle import Turtle

ALIGNMENT = "center"
FONT = "Arial"
STYLE = "normal"


class ScoreBoard(Turtle):
    """Creating the scoreboard class"""

    def __init__(self, score):
        self.score = score
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Method for updating the scoreboard"""
        self.write(
            f"Score: {self.score}",
            move=False,
            align=ALIGNMENT,
            font=(FONT, 8, STYLE),
        )

    def game_over(self):
        """Method for printing game over"""
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            move=False,
            align=ALIGNMENT,
            font=(FONT, 12, STYLE),
        )

    def increase_score(self):
        """Method for increasing the score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()
