from abc import abstractmethod
import math


class GameObject:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def move(self, x, y):
        self.pos_x = x
        self.pos_y = y

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass

    @abstractmethod
    def handle_events(self):
        pass
