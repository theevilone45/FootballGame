from GameLoop import GameLoop
import pygame
import os


class FootballGame(GameLoop):
    def load_resources(self):
        self.pitch_image = pygame.image.load(os.path.join("GameEngine", "Images", "pitch.jpg"))
        self.pitch_rect = self.pitch_image.get_rect()
        pass

    def init_objects(self):
        pass

    def __init__(self):
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.pitch_image = None
        self.pitch_rect = None

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
        self.screen.blit(self.pitch_image, self.pitch_rect)

        # draw everything
        for obj in self.objects:
            obj.render(self.screen)

        pygame.display.flip()
        self.clock.tick(self.fps)
        pass
