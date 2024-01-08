import pygame
import sys


class NewWindow:
    def __init__(self):
        pygame.init()
        self.fon = pygame.image.load("data/snow.jpg")
        self.maus_img = pygame.image.load("data/litle_mouse.png")
        self.rect_maus = self.maus_img.get_rect()
        self.mouse_die = 1 # флаг убийсва крысы, пока зеленый всегда

    def run(self):
        self.fon = pygame.transform.scale(self.fon, (1300, 750))
        self.width, self.height = self.fon.get_width(), self.fon.get_height()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("New Window")
        self.rect_maus.topleft = (1000, 300)
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_m:
                #         self.m = True

            self.screen.blit(self.fon, (0, 0))
            pygame.display.flip()

            if self.mouse_die:
                self.fal()

    def fal(self):
        clock = pygame.time.Clock()

        fall_speed = 2
        falling = True
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.rect_maus.y += fall_speed

            if self.rect_maus.y >= self.height - 60:
                falling = False

            self.screen.blit(self.fon, (0, 0))

            if falling:
                self.screen.blit(self.maus_img, self.rect_maus)

            pygame.display.flip()
            clock.tick(70)

        pygame.quit()


if __name__ == "__main__":
    window = NewWindow()
    window.run()
