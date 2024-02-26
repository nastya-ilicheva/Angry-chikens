import pygame
import sys


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

        pygame.display.update()


if __name__ == "__main__":
    window = FinalWindow()
    window.run()
