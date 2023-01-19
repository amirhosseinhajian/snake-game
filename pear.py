from food import Food

class Pear(Food):
    def __init__(self, game):
        super().__init__(game, 2, "./images/pear.png")