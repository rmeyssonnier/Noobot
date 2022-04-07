import cv2 as cv


class Entity:
    def __init__(self, name, picture) -> None:
        self.name = name
        self.picture = picture
        self.template = cv.imread(picture, 0)
        self.width, self.height = self.template.shape[::-1]
