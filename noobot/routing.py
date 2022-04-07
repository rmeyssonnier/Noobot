from noobot.movement import Movement
from noobot.position import Position


class RectangleRouting:
    horizontal_direction = Movement.RIGHT
    vertical_direction = Movement.DOWN

    def __init__(self, game_position, end_position) -> None:
        self.game_position = game_position
        self.end_position = end_position
        self.start_position = Position(game_position.position.x, game_position.position.y)

    def next_move(self):
        next_movement = Movement.RIGHT
        current_position = self.game_position.position

        if self.horizontal_direction == Movement.RIGHT and current_position.x < self.end_position.x:
            next_movement = Movement.RIGHT

        if self.horizontal_direction == Movement.LEFT and current_position.x > self.start_position.x:
            next_movement = Movement.LEFT

        if current_position.x == self.end_position.x and self.horizontal_direction == Movement.RIGHT:
            if current_position.y == self.start_position.y:
                self.vertical_direction = Movement.DOWN

            if current_position.y == self.end_position.y:
                next_movement = Movement.LEFT
            else:
                next_movement = self.vertical_direction

            self.horizontal_direction = Movement.LEFT

        if current_position.x == self.start_position.x and self.horizontal_direction == Movement.LEFT:

            if current_position.y == self.end_position.y:
                self.vertical_direction = Movement.TOP

            if current_position.y == self.start_position.y:
                next_movement = Movement.RIGHT
            else:
                next_movement = self.vertical_direction

            self.horizontal_direction = Movement.RIGHT

        print(next_movement)
        self.game_position.move(next_movement)