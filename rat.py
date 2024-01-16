import pygame


class Rat:
    def __init__(self, x, y, height, width, fon, screen):
        pygame.init()
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.fon = fon
        self.screen = screen
        self.maus_img = pygame.image.load("data/litle_mouse.png")
        self.rect_maus = self.maus_img.get_rect()
        self.mouse_die = 1  # флаг убийсва крысы, пока зеленый всегда

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
