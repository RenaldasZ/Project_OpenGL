import pygame
import sys
from core.input import Input

class Base(object):

    def __init__(self):

        # initialize all pygame modules
        pygame.init()

        # width and heigh of window
        screenSize = (512, 512)

        # indicate rendering options
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL

        # create and display the window
        self.screen = pygame.display.set_mode(screenSize, displayFlags)

        # set the text that appears in title bar of window
        pygame.display.set_caption("Graphics Window")

        # determines if main loop is active
        self.running = True

        # manage time-related data and operations
        self.clock = pygame.time.Clock()

        # manage user input
        self.input = Input()

    # implement by extending class
    def initialize(self):
        pass

    # implement by extending class
    def update(self):
        pass

    def run(self):

        ## startup ##
        self.initialize()

        ## main loop ##
        while self.running:

            ## process input ##
            self.input.update()

            if self.input.quit:
                self.running = False

            ## update ##
            self.update()

            ## render ##

            # display image on screen
            pygame.display.flip()

            # pause if necessary to achieve 60 FPS
            self.clock.tick(60)

        ## shutdown ##
        pygame.quit()
        sys.exit()
