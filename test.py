import pygame
import sys
from button import Button
from level_1 import NewWindow


class BasicWindow:
    def __init__(self):
        pygame.init()
        self.fon = pygame.image.load("data/ligts.jpg")

    # def text(self):
    #     font = pygame.font.Font('data/better-vcr-5.4.ttf', 32)
    #     with open("data/chicen - pyki.txt") as f:
    #         for i, line in enumerate(f):
    #             text_surface = font.render(line, True, '#FFFF66')
    #             text_rect = text_surface.get_rect()
    #             text_rect.center = (200, 200)
    #             self.screen.blit(text_surface, text_rect)

    def background_image(self):
        self.fon = pygame.transform.scale(self.fon, (1300, 750))
        self.image = self.fon
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Angry chikens")
        font = pygame.font.Font('data/better-vcr-5.4.ttf', 32)
        with open("data/chicen - pyki.txt") as f:
            for i, line in enumerate(f):
                text_surface = font.render(line, True, '#FFFF66')
                text_rect = text_surface.get_rect()
                text_rect.center = (200, 200)
                #self.screen.blit(text_surface, text_rect)

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen = self.image, (0, 0)
            #self.screen.blit(text_surface, text_rect)

            button_level_1 = Button()
            button_level_1.create_button(self.screen, '#FFFF66', 1100, 75, 100, 50, 0, "level_1", "#7D00DC")

            button_level_2 = Button()
            button_level_2.create_button(self.screen, '#FFFF66', 1100, 175, 100, 50, 0, "level_2", "#7D00DC")

            button_level_3 = Button()
            button_level_3.create_button(self.screen, '#FFFF66', 1100, 275, 100, 50, 0, "level_3", "#7D00DC")

            button_level_4 = Button()
            button_level_4.create_button(self.screen, '#FFFF66', 1100, 375, 100, 50, 0, "level_4", "#7D00DC")

            button_level_5 = Button()
            button_level_5.create_button(self.screen, '#FFFF66', 1100, 475, 100, 50, 0, "level_5", "#7D00DC")
            pygame.display.flip()
            pygame.display.update()


if __name__ == "__main__":
    window = BasicWindow()
    window.background_image()
    # window.text()
