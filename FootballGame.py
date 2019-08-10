from GameLoop import GameLoop
import pygame
from Objects.Ball import Ball


class FootballGame(GameLoop):
    def load_resources(self):
        pass

    def init_objects(self):
        self.objects.append(Ball(100, 100, 10, (255, 0, 0)))
        pass

    def __init__(self):
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

        # draw everything
        for obj in self.objects:
            obj.render(self.screen)

        pygame.display.flip()
        self.clock.tick(self.fps)
        pass
