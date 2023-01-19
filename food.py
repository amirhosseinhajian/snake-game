import arcade
import random

class Food(arcade.Sprite):
    def __init__(self, game, score, vector):
        super().__init__(vector)
        self.width = 24
        self.height =24
        self.score = score
        self.center_x = random.randint(10, game.width-10)
        self.center_y = random.randint(10, game.height-10)
        self.change_x = 0
        self.change_y = 0