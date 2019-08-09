from abc import abstractmethod


class GameLoop:
    def __init__(self):
        self.is_open = True

    def start(self):
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
