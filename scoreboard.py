from turtle import Turtle




class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = data.read()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", move=False, align='center', font=('Courier', 20, 'normal'))


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=('Courier', 20, 'normal'))

    def reset(self):
        #data = open("data.txt", "w")
        #high_score = data.read()

        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))

        #    print(type(high_score))
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    #def reset_game(self):
    #    self.high_score = 0
    #    with open("data.txt", mode="w") as data:
    #        data.write(str(self.high_score))