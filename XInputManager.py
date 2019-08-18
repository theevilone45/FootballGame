import pygame

BTN_MAP = {
    'A': 0,
    'B': 1,
    'X': 2,
    'Y': 3,
    'LEFT_BUMP': 4,
    'RIGHT_BUMP': 5,
    'MENU': 6,
    'VIEW': 7,
    'LS': 8,
    'RS': 9
}


class Controller:
    def __init__(self, index):
        self.joystick = pygame.joystick.Joystick(index)
        self.joystick.init()
        self.number_of_axes = self.joystick.get_numaxes()
        self.number_of_buttons = self.joystick.get_numbuttons()
        pass

    def show_info(self):
        print("Axes: " + str(self.number_of_axes))
        print("Buttons: " + str(self.number_of_buttons))

    def get_axis(self, index):
        return self.joystick.get_axis(index)

    def get_button_state(self, index):
        return self.joystick.get_button(index)

    pass
