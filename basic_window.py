import pygame
import sys
from button import Button
from level_1 import NewWindow


class BasicWindow:
    def __init__(self):
        pygame.init()
        self.fon = pygame.image.load("data/ligts.jpg")

    def background_image(self):
        self.fon = pygame.transform.scale(self.fon, (1300, 750))
        self.image = self.fon
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("angry chikens")

        self.screen.blit(self.image, (0, 0))

        # создание кнопок
        button_level_1 = Button()
        button_level_1.create_button(self.screen, "blue", 50, 50, 100, 50, 0, "level_1", "black")

        button_level_2 = Button()
        button_level_2.create_button(self.screen, "blue", 200, 50, 100, 50, 0, "level_2", "black")

        button_level_3 = Button()
        button_level_3.create_button(self.screen, "blue", 350, 50, 100, 50, 0, "level_3", "black")

        button_level_4 = Button()
        button_level_4.create_button(self.screen, "blue", 500, 50, 100, 50, 0, "level_4", "black")

        button_level_5 = Button()
        button_level_5.create_button(self.screen, "blue", 650, 50, 100, 50, 0, "level_5", "black")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_level_1.pressed(pygame.mouse.get_pos()):
                        new_window = NewWindow()
                        new_window.run()

            pygame.display.update()


if __name__ == "__main__":
    window = BasicWindow()
    window.background_image()
