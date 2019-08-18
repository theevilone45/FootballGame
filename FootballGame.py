from GameLoop import GameLoop
import pygame
import os
from Objects.Ball import Ball
from Objects.Human import Human


class FootballGame(GameLoop):
    def load_resources(self):
        self.images['pitch'] = pygame.transform.scale(
            pygame.image.load(os.path.join("GameEngine", "Images", "pitch.jpg")), self.resolution)
        self.rects['pitch'] = self.images['pitch'].get_rect()

        self.images['ball'] = pygame.transform.scale(
            pygame.image.load(os.path.join("GameEngine", "Images", "ball.png")), (10, 10))
        self.rects['ball'] = self.images['ball'].get_rect()
        pass

    def init_objects(self):
        self.objects.append(Ball(200, 200, 10, (150, 150, 150)))
        self.objects.append(Human(100, 100, (0, 0, 0), 3))
        pass

    def __init__(self):
        super().__init__()
        pygame.init()
        if self.full_screen:
            self.screen = pygame.display.set_mode(self.resolution, pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.images = dict()
        self.rects = dict()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_open = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_open = False
        for obj in self.objects:
            obj.handle_events()
        pass

    def update(self):
        for obj in self.objects:
            obj.update()
        pass

    def render(self):
        self.screen.fill(self.background_color)
        self.screen.blit(self.images['pitch'], self.rects['pitch'])

        # draw everything
        for obj in self.objects:
            obj.render(self.screen)

        pygame.display.flip()
        self.clock.tick(self.fps)
        pass
