from abc import abstractmethod


class GameObject:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def handle_events(self):
        pass
