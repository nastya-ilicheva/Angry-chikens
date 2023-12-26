import pygame
import sys


class NewWindow:
    def __init__(self):
        pygame.init()
        self.fon = pygame.image.load("snow.jpg")


    def run(self):
        self.fon = pygame.transform.scale(self.fon, (1300, 750))
        self.image = self.fon
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("new")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.image, (0, 0))
            pygame.display.flip()
