import pygame
import sys

import b2.settings
from button import Button
from b2.settings import LEVEL_COMPLETED


class FinalWindow:
    def __init__(self):
        pygame.init()
        self.fon = pygame.image.load("data/finish_wind_picture.png")

    def run(self):
        self.fon = pygame.transform.scale(self.fon, (1300, 750))
        self.image = self.fon
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("☠️Game_is_over☠️")
        self.screen.blit(self.image, (0, 0))

        t = 'Congratulations! & You have completed the game with dignity & and able to stole ALL eggS! &  & HERE NASTYA ARE MAKING &  AGAIN PLAY BUTTON'
        y = 190

        text = t.split('&')

        button_again = Button()
        button_again.create_button(self.screen, 'white', 0, 0, 100, 50, 0, "again", "#1E90FF")

        for i in text:
            i = i.strip()
            myFont = pygame.font.SysFont('maiandragd', 35)
            myText = myFont.render(i, 1, '#FFF921')
            self.screen.blit(myText, (50, y))
            y += 40
            pygame.display.update()

        running = True
        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif button_again.pressed(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(LEVEL_COMPLETED)):
                        LEVEL_COMPLETED[i] = 0
                    b2.settings.COUNT = 0
                    running = False

        pygame.display.update()


if __name__ == "__main__":
    window = FinalWindow()
    window.run()
