import arcade
from snake import Snake
from apple import Apple
from pear import Pear
from poop import Poop

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Snake")
        arcade.set_background_color(arcade.color.DARK_KHAKI)
        self.apple = Apple(self)
        self.pear = Pear(self)
        self.poop = Poop(self)
        self.snake = Snake(self)
        self.is_game_ended = False
        self.target = self.calculate_shortest_distance()
    
    def on_draw(self):
        arcade.start_render()
        self.apple.draw()
        self.pear.draw()
        self.poop.draw()
        self.snake.draw()
        arcade.draw_text(f"Score: {self.snake.score}", 10, 20, arcade.color.WHITE, 14)
        if self.is_game_ended == True:
            arcade.draw_text("GAME OVER", 133, 250, arcade.color.DARK_BLUE, 28)
        arcade.finish_render()

    def on_update(self, delta_time: float):
        if not self.is_game_ended:
            if self.snake.center_y > self.target.center_y+10 and self.snake.change_y != 1:
                self.snake.change_x = 0
                self.snake.change_y = -1
            elif self.snake.center_x < self.target.center_x and self.snake.change_x != -1:
                self.snake.change_x = 1
                self.snake.change_y = 0
            elif self.snake.center_y < self.target.center_y-10 and self.snake.change_y != -1:
                self.snake.change_x = 0
                self.snake.change_y = 1
            elif self.snake.center_x > self.target.center_x and self.snake.change_x != 1:
                self.snake.change_x = -1
                self.snake.change_y = 0
        if not self.is_game_ended:
            self.snake.move()
            if arcade.check_for_collision(self.snake, self.apple):
                self.snake.eat(self.apple)
                self.apple = Apple(game)
                self.target = self.calculate_shortest_distance()
            if arcade.check_for_collision(self.snake, self.pear):
                self.snake.eat(self.pear)
                self.pear = Pear(game)
                self.target = self.calculate_shortest_distance()
            if arcade.check_for_collision(self.snake, self.poop):
                self.snake.eat(self.poop)
                self.poop = Poop(game)
            if self.snake.score < 1 or self.snake.center_x < 10 or self.snake.center_x > self.width-10 or self.snake.center_y < 10 or self.snake.center_y > self.height-10:
                self.is_game_ended = True
            for i in range(len(self.snake.body)-14, 0, -1):
                if arcade.check_for_collision(self.snake, self.snake.body[i]):
                    self.is_game_ended = True

    def calculate_shortest_distance(self):
        apple_distance = arcade.get_distance(self.snake.center_x, self.snake.center_y, self.apple.center_x, self.apple.center_y)
        pear_distance = arcade.get_distance(self.snake.center_x, self.snake.center_y, self.pear.center_x, self.pear.center_y)
        if apple_distance < pear_distance:
            return self.apple
        return self.pear

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            if not self.snake.change_y:
                self.snake.change_x = 0
                self.snake.change_y = 1
        elif symbol == arcade.key.DOWN:
            if not self.snake.change_y:
                self.snake.change_x = 0
                self.snake.change_y = -1
        elif symbol == arcade.key.RIGHT:
            if not self.snake.change_x:
                self.snake.change_x = 1
                self.snake.change_y = 0
        elif symbol == arcade.key.LEFT:
            if not self.snake.change_x:
                self.snake.change_x = -1
                self.snake.change_y = 0

if __name__ == "__main__":
    game = Game()
    arcade.run()