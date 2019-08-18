from Objects.GameObject import GameObject


class Human(GameObject):
    def update(self):
        pass

    def render(self, screen):
        pass

    def handle_events(self, args=None):

        pass

    def __init__(self, x, y, color, speed):
        super().__init__(x, y)
        self.color = color
        self.speed = speed

    pass
