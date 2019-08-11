from abc import abstractmethod


class GameLoop:
    def __init__(self):
        self.is_open = True
        self.background_color = (0, 0, 0)
        self.fps = 60
        self.resolution = (800, 600)
        self.objects = []

    def start(self):
        self.load_resources()
        self.init_objects()

        while self.is_open:
            self.handle_events()
            self.update()
            self.render()

    @abstractmethod
    def handle_events(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def load_resources(self):
        pass

    @abstractmethod
    def init_objects(self):
        pass
