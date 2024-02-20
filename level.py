import pygame as pg
import sys

from b2.functions import screen_to_world, world_to_screen
from Box2D.b2 import world, polygonShape, circleShape
from b2 import settings
import util
from levels import *
from button import Button
# from main import StartWindow

# pygame.init()
# world = world(gravity=(0, -0.5))


class NewWindow:
    def __init__(self, level_number, name_window):

        self.world = world(gravity=(0, -0.5))

        self.level_number = level_number
        self.name_window = name_window

        self.fon = pygame.image.load("data/snow.jpg")
        self.all_sprites = pygame.sprite.Group()  # создаем группу спрайтов для всех спрайтов

        self.bricks = []  # список для хранения ссылок на спрайты

        bar_body = self.world.CreateStaticBody(position=(29, -28), shapes=polygonShape(box=(20, 1)))
        brick_sprite = Brick(self.all_sprites, bar_body)
        self.bricks.append(brick_sprite)  # сохраняем ссылку на спрайт




    def run(self):
        self.fon = pygame.transform.scale(self.fon, (1300, 750))
        self.width, self.height = self.fon.get_width(), self.fon.get_height()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name_window)

        MYEVENTTYPE = pygame.USEREVENT + 1
        pygame.time.set_timer(MYEVENTTYPE, 4)

        create_bird_event = pygame.USEREVENT + 24
        pygame.time.set_timer(create_bird_event, 10000)

        all_sprites = pygame.sprite.Group()
        bird_sprites = pygame.sprite.Group()

        util.screen = screen
        polygonShape.draw = util.my_draw_polygon
        circleShape.draw = util.my_draw_circle

        if self.level_number == 1:
            center_body, bird, rat, bird_count = level_1(self.world, all_sprites, bird_sprites)
        elif self.level_number == 2:
            center_body, bird, rat, bird_count = level_2(self.world, all_sprites, bird_sprites)
        elif self.level_number == 3:
            center_body, bird, rat, bird_count = level_3(self.world, all_sprites, bird_sprites)

        button_back = Button()
        button_back.create_button(self.fon, 'white', 0, 0, 100, 50, 0, "back", "#1E90FF")


        flag1 = False
        running = True
        moving = 0
        kill_bird = False
        line = True
        died = False
        life = True

        pygame.mixer.music.load('data/chiken_music.mp3')
        pygame.mixer.music.play()

        catapult = pg.image.load('data/catapult.png')
        scale = pygame.transform.scale(
            catapult, (catapult.get_width() // 2,
                       catapult.get_height() // 2))
        scale_rect = scale.get_rect(center=(world_to_screen((-40, -26))))
        screen.blit(scale, scale_rect)

        while running:
            print(f"life: {life}")
            print(f"died {died}")
            #print(RAT.rect.center)
            if died:
                print('died')
                settings.COUNT += 1
                return True
                # sys.exit()
                # RAT.kill()
                # world.DestroyBody(RAT.body)
                died = False
                # NewWindow2().run2()
            if rat.rect.center[1] >= settings.SCREEN_HEIGHT and life:
                died = True
                life = False
                print(f"life1: {life}")
                print(f"died1 {died}")
            #life = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_back.pressed(pygame.mouse.get_pos()):
                        # pygame.quit()
                        # sys.exit()
                        # running = False
                        return False


                if event.type == MYEVENTTYPE:
                    bird_sprites.update(True)
                    all_sprites.update()

                if event.type == create_bird_event and kill_bird:
                    bird.sprite.kill()
                    self.world.DestroyBody(bird.sprite.body)
                    center_body = self.world.CreateStaticBody(
                        position=(-40, -20),
                        shapes=polygonShape(box=(0.2, 0.2)))

                    if bird_count < 2:
                        bird = FlyBird(self.world, bird_sprites, center_body, "data/litle_red_bird.png")
                        bird_count += 1
                    kill_bird = False
                    line = True
                    moving = 0

                # реализация катапульты (удаление всех джоинтов для полета птицы)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and moving == 0:
                    moving = 1
                if event.type == pygame.MOUSEMOTION:
                    if moving == 1:
                        bird.mJoint.target = screen_to_world(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and moving == 1:
                    moving = 2
                    self.world.DestroyJoint(bird.rope)
                    self.world.DestroyJoint(bird.mJoint)
                    flag1 = True


                if flag1:
                    if (bird.ball_body.position.x - bird.center_body.position.x) ** 2 + (
                            bird.ball_body.position.y - bird.center_body.position.y) ** 2 < 4:
                        self.world.DestroyJoint(bird.joint)
                        self.world.DestroyBody(center_body)
                        flag1 = False
                        line = False
                        kill_bird = True

            screen.fill((0, 0, 0, 0))
            util.draw_bodies(self.world)
            screen.blit(self.fon, (0, 0))

            catapult = pg.image.load('data/catapult.png')
            scale = pygame.transform.scale(
                catapult, (catapult.get_width() // 2,
                           catapult.get_height() // 2))
            scale_rect = scale.get_rect(center=(world_to_screen((-40, -26))))
            screen.blit(scale, scale_rect)

            if line:
                pygame.draw.line(screen, (53, 23, 12), (world_to_screen((-38, -18))), bird.sprite.rect.center, 8)
                pygame.draw.line(screen, (53, 23, 12), (world_to_screen((-42, -18))), bird.sprite.rect.center, 8)

            # world.Step(TIME_STEP, 10, 10)

            self.world.Step(settings.TIME_STEP, 10, 10)
            all_sprites.update()
            all_sprites.draw(screen)
            bird_sprites.draw(screen)
            pygame.display.flip()
            # if self.c == 3 and died:
            #     NewWindow2().run2()
            #     self.level = 2
            # elif self.c == 3 and died == False:


            # clock.tick(TARGET_FPS)


if __name__ == "__main__":
    window = NewWindow(1, "hgfcjgfcg")
    window.run()