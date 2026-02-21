from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.high_score = []
        self.highscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 300)
        self.write(self.p1_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 300)
        self.write(self.p2_score, align="center", font=("Courier", 40, "normal"))

    def p1_point(self):
        self.p1_score += 1
        self.update_scoreboard()

    def p2_point(self):
        self.p2_score += 1
        self.update_scoreboard()




# ONGOING CHANGES
    def highscore(self):
        with open("highscores.txt") as f:
            temp = f.readlines()
            for person in temp:
                self.high_score.append(person.split(","))

    def update_highscore(self):
        self.high_score[0][1] = "4\n"
        with open('test12.txt', "w") as f:
            for person in self.high_score:
                f.write(person[0] + "," + person[1])