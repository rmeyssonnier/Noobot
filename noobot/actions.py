from time import sleep

import pyautogui


class CollectAction:
    farm_cooldown = 10

    def __init__(self) -> None:
        pass

    def collect_ressource(self, entity, position):
        pyautogui.moveTo(position.x, position.y, 1)
        pyautogui.leftClick()
        sleep(self.farm_cooldown)
