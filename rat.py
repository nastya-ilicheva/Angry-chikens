import pygame


class Rat(pygame.sprite.Sprite):

    def __init__(self, x, y, height, width, fon, screen, all_sprites):
        super().__init__(all_sprites)
        pygame.init()
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.fon = fon
        self.screen = screen
        self.image = pygame.image.load("data/litle_mouse.png")
        self.rect = self.image.get_rect()
        # self.rect_maus.topleft = (1000, 300)
        self.rat_die = 1  # флаг убийсва крысы, пока зеленый всегда

    def update(self):
        # if not pygame.sprite.collide_mask(self, mountain):
        print(self.rect.center)
        self.rect = self.rect.move(0, 1)
