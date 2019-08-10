from Objects.GameObject import GameObject
import pygame
import math
import random


class Ball(GameObject):
    def update(self):
        self.pos_x += self.force * math.cos(self.angle)
        self.pos_y += self.force * math.sin(self.angle)
        self.force *= 0.99
        width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
        if self.pos_y <= self.radius or self.pos_y > height-self.radius:
            self.angle = 2*math.pi-self.angle
        if self.pos_x <= self.radius or self.pos_x > width-self.radius:
            self.angle = math.pi-self.angle
        pass

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos_x), int(self.pos_y)), self.radius)
        pass

    def handle_events(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            self.apply_force(random.uniform(0, 2 * math.pi), random.uniform(1, 6))
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
        pass
