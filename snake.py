import arcade

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 24
        self.height = 24
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color_1 = arcade.color.BLUE
        self.color_2 = arcade.color.RED
        self.change_x = 0
        self.change_y = 0
        self.speed = 5
        self.score = 1
        self.body = arcade.SpriteList()

    def move(self):
        new_body_part = arcade.Sprite(center_x=self.center_x, center_y=self.center_y)
        new_body_part.width = self.width
        new_body_part.height = self.height
        self.body.append(new_body_part)
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def eat(self, food):
        self.score += food.score
        del food

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color_1)
        self.body.reverse()
        for index, part in enumerate(self.body):
            arcade.draw_rectangle_filled(part.center_x, part.center_y, part.width, part.height, self.color_1 if index%2!=0 else self.color_2)
        self.body.reverse()
