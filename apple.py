from food import Food

class Apple(Food):
    def __init__(self, game):
        super().__init__(game, 1, "./images/apple.png")
        self.scale = 0.02