import pygame
import sys
from rat import Rat
from catapult import Catapult

pygame.init()


class NewWindow:
    def __init__(self):

        self.fon = pygame.image.load("data/snow.jpg")

    def run(self):
        self.fon = pygame.transform.scale(self.fon, (1300, 750))
        self.width, self.height = self.fon.get_width(), self.fon.get_height()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("New Window")

        MYEVENTTYPE = pygame.USEREVENT + 1
        pygame.time.set_timer(MYEVENTTYPE, 4)

        all_sprites = pygame.sprite.Group()
        Rat(100, 10, self.height, self.width, self.fon, self.screen, all_sprites)
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MYEVENTTYPE:
                    all_sprites.update()

            self.screen.blit(self.fon, (0, 0))

            all_sprites.draw(self.screen)
            pygame.display.flip()


if __name__ == "__main__":
    window = NewWindow()
    window.run()
