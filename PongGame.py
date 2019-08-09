from GameLoop import GameLoop
import pygame


class PongGame(GameLoop):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.background_color = (0, 0, 0)
        self.fps = 60
        self.resolution = (800, 600)
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_open = False

        # keyboard input
        self.key_pressed(pygame.key.get_pressed())
        pass

    def key_pressed(self, pressed):
        pass

    def update(self):

        pass

    def render(self):
        self.screen.fill(self.background_color)

        # draw everything

        pygame.display.flip()
        self.clock.tick(self.fps)
        pass
