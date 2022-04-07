from time import sleep

import pyautogui as pyautogui

from noobot.movement import Movement
from noobot.position import Position


class Player:
    position = Position(0, 0)

    def __init__(self, initial_position) -> None:
        self.position = initial_position

    def move(self, movement) -> None:
        if movement == Movement.TOP:
            pyautogui.moveTo(1024, 60, 1)
            self.position.y = self.position.y - 1
        elif movement == Movement.RIGHT:
            pyautogui.moveTo(1570, 540, 1)
            self.position.x = self.position.x + 1
        elif movement == Movement.DOWN:
            pyautogui.moveTo(1024, 910, 1)
            self.position.y = self.position.y + 1
        elif movement == Movement.LEFT:
            pyautogui.moveTo(30, 540, 1)
            self.position.x = self.position.x - 1

        pyautogui.leftClick()
