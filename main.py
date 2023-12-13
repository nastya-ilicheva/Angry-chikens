import pygame
import sys


class BasicWindow:
    def __init__(self):
        pygame.init()
        self.fon = pygame.image.load("snow.jpg")

    def background_image(self):
        self.fon = pygame.transform.scale(self.fon, (1600, 950))
        self.im = self.fon
        self.w, self.h = self.im.get_width(), self.im.get_height()
        self.screen = pygame.display.set_mode((self.w, self.h))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.im, (0, 0))

            pygame.display.update()


if __name__ == "__main__":
    window = BasicWindow()
    window.background_image()
