import random
import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SNAKE_SPPED = 1.7

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 10
        self.height = 10
        self.color = arcade.color.WHITE
        self.body_size = 0
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.speed = SNAKE_SPPED
        self.body_parts = []
        self.direction = "right"

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

    def move(self):
        for part in range(len(self.body_parts)-1, 0,-1):
            new_center_x = self.body_parts[part-1].center_x
            new_center_y = self.body_parts[part - 1].center_y
            self.body_parts[part].center_x = new_center_x
            self.body_parts[part].center_y = new_center_y
        if self.direction == "right":
            self.center_x += self.speed
        elif self.direction == "left":
            self.center_x -= self.speed
        elif self.direction == "up":
            self.center_y += self.speed
        elif self.direction == "down":
            self.center_y -= self.speed


class Food(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = random.randint(10, 480)
        self.center_y = random.randint(10, 480)
        texture = arcade.load_texture("pear.png")
        self.texture = texture
        self.scale = 0.049

    def draw(self):
        arcade.draw_texture_rectangle(self.center_x, self.center_y, 30, 30, self.texture)

class Poop(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = random.randint(10, 480)
        self.center_y = random.randint(10, 480)
        texture = arcade.load_texture("poop.png")
        self.texture = texture
        self.scale = 0.049

    def draw(self):
        arcade.draw_texture_rectangle(self.center_x, self.center_y, 24, 24, self.texture)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Snake Game")
        arcade.set_background_color(arcade.color.DARK_CYAN)
        self.score = 1
        self.game_is_on = True
        self.snake = Snake()
        self.snake.color = arcade.color.RED
        self.snake.body_parts.append(self.snake)
        self.food = Food()
        self.poop = Poop()
        for i in range(0, 3):
            self.body_update()

    def on_draw(self):
        arcade.start_render()
        for part in self.snake.body_parts:
            part.draw()
        self.food.draw()
        self.poop.draw()
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)
        if self.game_is_on == False:
            arcade.draw_text("GAME OVER", 133, 250, arcade.color.LEMON, 28)

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            if self.snake.direction != "right":
                self.snake.direction = "left"
        elif key == arcade.key.RIGHT:
            if self.snake.direction != "left":
                self.snake.direction = "right"
        elif key == arcade.key.UP:
            if self.snake.direction != "down":
                self.snake.direction = "up"
        elif key == arcade.key.DOWN:
            if self.snake.direction != "up":
                self.snake.direction = "down"

    def body_update(self):
        for i in range(0, 8):
            new_part = Snake()
            new_part.center_x = self.snake.body_parts[-1].center_x
            new_part.center_y = self.snake.body_parts[-1].center_y
            self.snake.body_parts.append(new_part)
            self.on_draw()

    def on_update(self, delta_time: 0.001):
        if self.snake.center_x >= 494 or self.snake.center_x <= 6 or self.snake.center_y >= 494 or self.snake.center_y <= 6:
            self.game_is_on = False

        if self.score == 0:
            self.game_is_on = False

        for i in range(25, len(self.snake.body_parts) - 1):
            if arcade.check_for_collision(self.snake, self.snake.body_parts[i]):
                self.game_is_on = False

        if self.game_is_on == False:
            return

        self.snake.move()
        if arcade.check_for_collision(self.snake, self.food):
            self.food.center_x = random.randint(10, 480)
            self.food.center_y = random.randint(10, 480)
            self.body_update()
            self.score += 2

        if arcade.check_for_collision(self.snake, self.poop):
            self.poop.center_x = random.randint(10, 480)
            self.poop.center_y = random.randint(10, 480)
            self.score -= 1


my_game = Game()
arcade.run()