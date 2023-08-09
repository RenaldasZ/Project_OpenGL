import pygame

class Input(object):

    def __init__(self):

        # has the user quit the application?
        self.quit = False

    def update(self):
        # iterate over all user input events (keyboard/mouse)
        #  that have occured since last time events checked
        for event in pygame.event.get():
            # quit event occurs by clicking button to close window
            if event.type == pygame.QUIT:
                self.quit = True
                