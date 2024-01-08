import pygame
import os
import sys


class AnimatedSprite(pygame.sprite.Sprite): # тут гивки куриц
    def __init__(self, sheet, columns, rows, x, y, group):
        super().__init__(group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(20, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def main():
    RedBird = 1 # флаги на выбор куриц
    White_Parrot = 1
    Vorona = 1
    pygame.init()
    running = True
    size = 1500, 1000
    screen = pygame.display.set_mode(size)
    screen.fill(('black'))
    all_sprites = pygame.sprite.Group()
    if RedBird == True:
        bird = AnimatedSprite(load_image("litle_red_bird.png"), 4, 1, 365, 25, all_sprites)
    if Vorona == True:
        bird = AnimatedSprite(load_image("vorona.png"), 8, 1, 205, 15, all_sprites)
    if White_Parrot == True:
        bird = AnimatedSprite(load_image("hen.png"), 4, 1, 15, 15, all_sprites)

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        screen.fill((50, 50, 150))
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(12) #будем менять\ться

    pygame.quit()


if __name__ == '__main__':
    main()
