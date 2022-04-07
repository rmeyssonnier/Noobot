from noobot.actions import CollectAction
from noobot.brain import Brain
from noobot.game_vision import GameVision
from noobot.player import Player
from noobot.position import Position
from noobot.routing import RectangleRouting


def main():
    player = Player(Position(-1, -27))
    destination = Position(2, -22)

    game_vision = GameVision()
    game_action = CollectAction()
    game_routing = RectangleRouting(player, destination)

    bot = Brain(game_vision, game_action, game_routing, player)
    bot.init_bot()
    bot.loop()


if __name__ == "__main__":
    main()
