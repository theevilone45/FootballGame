from abc import abstractmethod
import pygame


class GameObject:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.win_width, self.win_height = pygame.display.Info().current_w, pygame.display.Info().current_h

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
    def handle_events(self, args=None):
        pass
