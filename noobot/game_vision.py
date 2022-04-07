import cv2 as cv
import numpy as np
import pyautogui

from noobot.position import Position
from noobot.tools import extract_text


def reduce_vision_result(arr, precision):
    filtered = []
    for v in arr:
        add = True
        for f in filtered:
            if v[0] in range(f[0] - precision, f[0] + precision, 1) and v[1] in range(f[1] - precision,
                                                                                      f[1] + precision, 1):
                add = False
                break
        if add:
            filtered.append(v)
    return filtered


class GameVision:
    to_track = []
    search_zone = [[370, 75], [1500, 860]]

    def __init__(self) -> None:
        pass

    def add_to_track(self, entity) -> None:
        self.to_track.append(entity)

    def get_current_position(self) -> Position:
        img = pyautogui.screenshot()
        r = extract_text(img)
        for p in r:
            for elem in p.split('\n'):
                if 'Niveau' in elem:
                    return Position(int(elem.split(',')[0]), int(elem.split(',')[1]))
        return Position(0, 0)

    def track_resources(self):
        vision_result = []
        for element in self.to_track:
            print('Track : ', element.name)
            # take a screenshot
            img = pyautogui.screenshot()
            # convert these pixels to a proper numpy array to work with OpenCV
            frame = np.array(img)
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            res = cv.matchTemplate(img_gray, element.template, cv.TM_CCOEFF_NORMED)
            threshold = 0.7
            loc = np.where(res >= threshold)

            cv_res = reduce_vision_result(zip(*loc[::-1]), 20)

            for pt in cv_res:
                to_click = [pt[0] + (element.width / 2), pt[1] + (element.height / 2)]
                print(pt)

                if to_click[0] > self.search_zone[0][0] and to_click[0] < self.search_zone[1][0] and to_click[1] > \
                        self.search_zone[0][1] and to_click[1] < self.search_zone[1][1]:
                    vision_result.append((element, Position(to_click[0], to_click[1])))

        return vision_result
