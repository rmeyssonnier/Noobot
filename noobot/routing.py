from noobot.movement import Movement
from noobot.position import Position


class AutoPiloteRouting:
    def __init__(self, game_position, destination) -> None:
        self.game_position = game_position
        self.destination = destination
        self.start_position = Position(game_position.position.x, game_position.position.y)

        self.previous_movement = Movement.LEFT

    def arrived(self):
        return self.game_position.position == self.destination

    def next_move(self):
        next_move = Movement.RIGHT
        dont_care_vertical = False
        dont_care_horizontal = False

        if self.game_position.position == self.destination:
            return

        dont_care_horizontal = (self.game_position.position.y == self.destination.y)
        dont_care_vertical = (self.game_position.position.x == self.destination.x)

        if (self.previous_movement == Movement.LEFT or self.previous_movement == Movement.RIGHT) or dont_care_vertical:
            if self.game_position.position.y < self.destination.y:
                next_move = Movement.DOWN
            else:
                next_move = Movement.TOP

        if (self.previous_movement == Movement.TOP or self.previous_movement == Movement.DOWN) or dont_care_horizontal:
            if self.game_position.position.x < self.destination.x:
                next_move = Movement.RIGHT
            else:
                next_move = Movement.LEFT

        self.game_position.move(next_move)
        self.previous_movement = next_move


class RectangleRouting:
    horizontal_direction = Movement.RIGHT
    vertical_direction = Movement.DOWN

    def __init__(self, game_position, destination) -> None:
        self.game_position = game_position
        self.destination = destination
        self.start_position = Position(game_position.position.x, game_position.position.y)

    def arrived(self):
        return False

    def next_move(self):
        next_movement = Movement.RIGHT
        current_position = self.game_position.position

        if self.horizontal_direction == Movement.RIGHT and current_position.x < self.destination.x:
            next_movement = Movement.RIGHT

        if self.horizontal_direction == Movement.LEFT and current_position.x > self.start_position.x:
            next_movement = Movement.LEFT

        if current_position.x == self.destination.x and self.horizontal_direction == Movement.RIGHT:
            if current_position.y == self.start_position.y:
                self.vertical_direction = Movement.DOWN

            if current_position.y == self.destination.y:
                next_movement = Movement.LEFT
            else:
                next_movement = self.vertical_direction

            self.horizontal_direction = Movement.LEFT

        if current_position.x == self.start_position.x and self.horizontal_direction == Movement.LEFT:

            if current_position.y == self.destination.y:
                self.vertical_direction = Movement.TOP

            if current_position.y == self.start_position.y:
                next_movement = Movement.RIGHT
            else:
                next_movement = self.vertical_direction

            self.horizontal_direction = Movement.RIGHT

        print(next_movement)
        self.game_position.move(next_movement)
