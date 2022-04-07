from noobot.actions import CollectAction
from noobot.brain import Brain
from noobot.game_vision import GameVision
from noobot.player import Player
from noobot.position import Position
from noobot.routing import RectangleRouting


def main():
    game_vision = GameVision()
    game_action = CollectAction()

    player = Player(game_vision.get_current_position())
    destination = Position(player.position.x + 3, player.position.y + 5)
    game_routing = RectangleRouting(player, destination)

    bot = Brain(game_vision, game_action, game_routing, player)
    bot.init_bot()
    bot.loop()


if __name__ == "__main__":
    main()
