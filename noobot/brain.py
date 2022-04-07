from time import sleep
from noobot.entity import Entity
from pynput import keyboard


class Brain:
    def __init__(self, game_vision, game_action, game_routing, player) -> None:
        self.keyboard_listener = None
        self.run = True
        self.game_vision = game_vision
        self.game_action = game_action
        self.game_routing = game_routing
        self.player = player

    def init_bot(self):
        ortie_entity = Entity('Ortie', './ressources/ortie.png')
        self.game_vision.add_to_track(ortie_entity)
        frene_entity = Entity('Frene', './ressources/frene.png')
        self.game_vision.add_to_track(frene_entity)

        self.keyboard_listener = keyboard.Listener(
            on_release=self.on_key_release)
        self.keyboard_listener.start()

        print('Bot init complete start from ', self.player.position, ' to ', self.game_routing.end_position)

    def loop(self):
        while True:
            if self.run:
                to_farm = self.game_vision.analyze_current_frame()
                for entity in to_farm:
                    self.game_action.collect_ressource(entity[0], entity[1])
                self.move()
            else:
                sleep(0.5)

    def move(self):
        start_pos = self.game_vision.get_current_position()
        new_pos = self.game_vision.get_current_position()
        self.game_routing.next_move()
        while start_pos == new_pos:
            new_pos = self.game_vision.get_current_position()
            sleep(0.5)

    def on_key_release(self, key):
        if key == keyboard.Key.ctrl:
            self.run = not self.run
            if self.run:
                print('Run bot')
            else:
                print('Pause bot')