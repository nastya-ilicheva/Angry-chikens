import pygame
import sys
from button import Button
from basic_window import BasicWindow


class StartWindow:
    def __init__(self):
        pygame.init()
        self.fon = pygame.image.load("data/ligts.jpg")

    def background_image(self):
        self.fon = pygame.transform.scale(self.fon, (1300, 750))
        self.image = self.fon
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("angry chikens")

        # создание кнопок
        button_start = Button()
        button_start.create_button(self.screen, "blue", 500, 200, 100, 50, 0, "start", "black")

        button_exit = Button()
        button_exit.create_button(self.screen, "blue", 500, 400, 100, 50, 0, "exit", "black")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_start.pressed(pygame.mouse.get_pos()):
                        new_window = BasicWindow()
                        new_window.background_image()
                    if button_exit.pressed(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()

            # self.screen.blit(self.image, (0, 0))
            pygame.display.update()


if __name__ == "__main__":
    window = StartWindow()
    window.background_image()
