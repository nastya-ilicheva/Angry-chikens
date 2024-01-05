import pygame
import sys
from button import Button
from basic_window import NewWindow


class StartWindow:
    def __init__(self):
        pygame.init()
        self.fon = pygame.image.load("data/lidhts.jpg")

    def background_image(self):
        self.fon = pygame.transform.scale(self.fon, (1300, 750))
        self.image = self.fon
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("angry chikens")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.image, (0, 0))

            # создание кнопок
            button = Button(20, 20, 50, 50, "dfjh", self.screen, self.open_new_window)
            button.draw()

            pygame.display.update()

    def open_new_window(self):
        new_window = NewWindow()
        new_window.run()



if __name__ == "__main__":
    window = StartWindow()
    window.background_image()