import pygame
import sys
from PIL import Image


class BasicWindow:
    def __init__(self):
        pygame.init()
        self.fon = "snow.jpg"

    def background_image(self):
        im = Image.open(self.fon)
        cropped_im = im.crop((250, 400, 1900, 1400))
        cropped_im.save("cropped_snow.jpg")

        self.im = pygame.image.load("cropped_snow.jpg")
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
