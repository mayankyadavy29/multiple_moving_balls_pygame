from config import height, width
from object import Object

class User(Object):
    def __init__(self, img, pos, speed):
        super().__init__(img, pos, speed)

    def move(self, up=False, down=False, left=False, right=False):
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if down:
            self.pos.top += self.speed
        if up:
            self.pos.top -= self.speed

        if self.pos.left < 0:
            self.pos.left = 0
        if self.pos.right > width:
            self.pos.right = width
        if self.pos.top < 0:
            self.pos.top = 0
        if self.pos.bottom > height:
            self.pos.bottom = height