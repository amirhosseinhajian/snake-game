from food import Food

class Poop(Food):
    def __init__(self, game):
        super().__init__(game, -1, "./images/poop.png")