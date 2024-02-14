import pygame
import sys
from button import Button
from level_1 import NewWindow


class BasicWindow:
    def __init__(self):
        pygame.init()
        self.fon = pygame.image.load("data/zastavka.jpg")
        self.font = pygame.font.Font('data/better-vcr-5.4.ttf', 32)

    def background_image(self):

        self.fon = pygame.transform.scale(self.fon, (1300, 820))
        self.image = self.fon
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Angry chikens")

        self.screen.blit(self.image, (0, 0))
        with open("data/chicen - pyki.txt") as f:
            for i in f:
                # myFont = pygame.font.SysFont('jokerman', 30)
                # myFont = pygame.font.SysFont('meiryo', 20)
                myFont = pygame.font.SysFont('pmingliuextb', 24)
                # myFont = pygame.font.SysFont('maiandragd', 30)
                # myFont = pygame.font.SysFont('poorrichard', 30)
                # myFont = pygame.font.SysFont('harrington', 22)
                # myText = myFont.render(i, 1, '#FFFF66')
                myText = myFont.render(i, 1, '#FFFF60')
                self.screen.blit(myText, (50, 70))

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
            button_level_1 = Button()
            button_level_1.create_button(self.screen, '#F5F5DC', 1133, 80, 100, 50, 0, "level 1", "#1E90FF")

            button_level_2 = Button()
            button_level_2.create_button(self.screen, '#FFF9BA', 1133, 160, 100, 50, 0, "level_2", "#1E90FF")

            button_level_3 = Button()
            button_level_3.create_button(self.screen, '#FFF590', 1133, 240, 100, 50, 0, "level_3", "#1E90FF")

            button_level_4 = Button()
            button_level_4.create_button(self.screen, '#FFEE4E', 1133, 320, 100, 50, 0, "level_4", "#1E90FF")

            button_level_5 = Button()
            button_level_5.create_button(self.screen, '#FFEA28', 1133, 400, 100, 50, 0, "level_5", "#1E90FF")

            pygame.display.update()


if __name__ == "__main__":
    window = BasicWindow()
    window.background_image()
