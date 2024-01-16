import pygame
import sys
from rat import Rat


class NewWindow:
    def __init__(self):
        pygame.init()
        self.fon = pygame.image.load("data/snow.jpg")

    def run(self):
        self.fon = pygame.transform.scale(self.fon, (1300, 750))
        self.width, self.height = self.fon.get_width(), self.fon.get_height()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("New Window")
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.fon, (0, 0))
            pygame.display.flip()

            mouse1 = Rat(1000, 300, self.height, self.width, self.fon, self.screen)
            if mouse1:
                mouse1.fal()


if __name__ == "__main__":
    window = NewWindow()
    window.run()
