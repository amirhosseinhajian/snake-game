import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110

arcade.open_window(400, 400, "Complex Loops - Box")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

for row in range(10):
    if row % 2 == 0:
        color1 = arcade.color.BLUE
        color2 = arcade.color.RED

    for column in range(10):
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN
        if column % 2 != 0:
            color1, color2 = color2, color1
        arcade.draw_rectangle_filled(x, y, 10, 10, color1, 45)

arcade.finish_render()
arcade.run()