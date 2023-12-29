import pygame
import sys
from button import Button
from basic_window import NewWindow
from finish_window import FinalWindow


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
                    # continue
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.image, (0, 0))

            # создание кнопок
            button_start = Button(600, 250, 120, 50, "старт", self.screen, self.open_new_window_basic())
            button_start.draw()
            button_settings = Button(595, 330, 130, 50, "настройки", self.screen, self.open_new_window_settings())
            button_settings.draw()
            button_quit = Button(600, 410, 120, 50, "выход", self.screen, self.close_window())
            button_quit.draw()

            pygame.display.update()

    def open_new_window_basic(self):
        new_window = NewWindow()
        new_window.run()

    def open_new_window_settings(self):
        new_window = FinalWindow()
        new_window.run()

    def close_window(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    window = StartWindow()
    window.background_image()
