from config import screen

class Object:
    def __init__(self, img, pos, speed):
        self.img = img
        self.speed = speed
        self.pos = img.get_rect().move((0, pos))
        screen.blit(self.img, self.pos)

    def move(self):
        """
        Override by child classes
        """
        pass