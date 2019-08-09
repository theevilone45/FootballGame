from Objects.GameObject import GameObject
import pygame
import math


class Ball(GameObject):
    def update(self):
        if self.force > 0:
            self.pos_x += self.force * math.cos(self.angle)
            self.pos_y += self.force * math.sin(self.angle)
        pass

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos_x), int(self.pos_y)), self.radius)
        pass

    def handle_events(self):
        pass

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
        pass
