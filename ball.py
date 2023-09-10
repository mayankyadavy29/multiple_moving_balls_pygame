from config import screen, width
from object import Object


class Ball(Object):
    def __init__(self, img, pos, speed):
        super().__init__(img, pos, speed)

    def move(self):
        self.pos = self.pos.move((self.speed, 0))
        if self.pos.left < 0 or self.pos.right > width:
            self.speed *= -1