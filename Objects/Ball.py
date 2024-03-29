from Objects.GameObject import GameObject
import pygame
import math
import random
from XInputManager import Controller


class Ball(GameObject):
    def update(self):
        if self.pos_y <= self.radius:
            self.angle = 2 * math.pi - self.angle
            self.pos_y = self.radius

        if self.pos_y > self.win_height - self.radius:
            self.angle = 2 * math.pi - self.angle
            self.pos_y = self.win_height - self.radius

        if self.pos_x <= self.radius:
            self.angle = math.pi - self.angle
            self.pos_x = self.radius

        if self.pos_x > self.win_width - self.radius:
            self.angle = math.pi - self.angle
            self.pos_x = self.win_width - self.radius

        self.pos_x += self.force * math.cos(self.angle)
        self.pos_y += self.force * math.sin(self.angle)
        self.force *= self.resistance
        pass

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos_x), int(self.pos_y)), self.radius)
        pass

    def handle_events(self, args=None):
        controller = Controller(0)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE] or controller.get_button_state(0) == 1:
            self.apply_force(random.uniform(0, 2 * math.pi), random.uniform(10, 20))
        pass

    # angle in radians
    def apply_force(self, angle, force):
        self.angle = angle
        self.force = force
        pass

    def __init__(self, x, y, radius, color):
        super().__init__(x, y)
        self.radius = radius
        self.color = color
        self.angle = 0
        self.force = 0
        self.resistance = 0.92
        pass
