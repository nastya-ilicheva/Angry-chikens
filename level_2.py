import pygame as pg
import sys
import asyncio

from b2.functions import screen_to_world, world_to_screen
from rat import Rat
# from catapult import Catapult
# from Box2D.b2 import world as box2d_world, polygonShape, circleShape, staticBody, dynamicBody
from Box2D.b2 import world, polygonShape, circleShape, staticBody, dynamicBody
from Box2D import b2RopeJointDef
from b2 import util, primitives, settings, classes, functions
from b2.primitives import *
# from level_1 import NewWindow
from catapult import FlyBird

pygame.init()
world = world(gravity=(0, -0.5))


class NewWindow2:
    def __init__(self):

        self.fon = pygame.image.load("data/snow.jpg")
        self.all_sprites = pygame.sprite.Group()  # создаем группу спрайтов для всех спрайтов

        self.bricks = []  # список для хранения ссылок на спрайты
        self.level = 2
        self.c = 0
        bar_body = world.CreateStaticBody(position=(29, -28), shapes=polygonShape(box=(20, 1)))
        brick_sprite = Brick(self.all_sprites, bar_body)
        self.bricks.append(brick_sprite)  # сохраняем ссылку на спрайт

    def run2(self):
        self.fon = pygame.transform.scale(self.fon, (1300, 750))
        self.width, self.height = self.fon.get_width(), self.fon.get_height()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("level 2👀")

        MYEVENTTYPE = pygame.USEREVENT + 1
        pygame.time.set_timer(MYEVENTTYPE, 4)

        create_bird_event = pygame.USEREVENT + 24
        pygame.time.set_timer(create_bird_event, 4000)

        all_sprites = pygame.sprite.Group()

        util.screen = screen
        polygonShape.draw = util.my_draw_polygon
        circleShape.draw = util.my_draw_circle

        bar_body = world.CreateStaticBody(position=(29, -28), shapes=polygonShape(box=(20, 1)))
        Brick(all_sprites, bar_body)  # пол

        brick_body = world.CreateDynamicBody(position=(19, -20))
        brick_body.CreatePolygonFixture(box=(5.5, 9), density=2, friction=1)
        Brick(all_sprites, brick_body)  # правая стена

        brick_body = world.CreateDynamicBody(position=(37, -20))
        brick_body.CreatePolygonFixture(box=(5.5, 9), density=1, friction=0.8)
        Brick(all_sprites, brick_body)  # левая стена

        brick_body = world.CreateDynamicBody(position=(28, -15))
        brick_body.CreatePolygonFixture(box=(21, 2), density=1, friction=1)
        Brick(all_sprites, brick_body)  # крыша
        #
        ball_body = world.CreateDynamicBody(position=(29, -8))
        ball_body.CreateCircleFixture(radius=6, density=1, friction=1, restitution=0.8)
        RAT = Ball(all_sprites, ball_body, scale=True)

        center_body = world.CreateStaticBody(
            position=(-40, -20),
            shapes=polygonShape(box=(0.5, 0.5)))

        bird_sprites = pygame.sprite.Group()
        bird = FlyBird(world, bird_sprites, center_body, "data/hen.png")

        flag1 = False
        running = True
        moving = 0
        kill_bird = False
        line = True
        died = False
        pygame.mixer.music.load('data/crazy-frog-axel-f-2005.mp3')
        pygame.mixer.music.play()

        catapult = pg.image.load('data/catapult.png')
        scale = pygame.transform.scale(
            catapult, (catapult.get_width() // 2,
                       catapult.get_height() // 2))
        scale_rect = scale.get_rect(center=(world_to_screen((-40, -26))))
        screen.blit(scale, scale_rect)

        while running:
            # if died:
            #     RAT.kill()
            #     world.DestroyBody(RAT.body)
            #     died = False
            # NewWindow().run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pg.quit()
                    sys.exit()

            # if pg.sprite.spritecollide(RAT, all_sprites, False):
            #     died = True

            if event.type == MYEVENTTYPE:
                bird_sprites.update(True)
                all_sprites.update()

            if event.type == create_bird_event and kill_bird:
                bird.sprite.kill()
                world.DestroyBody(bird.sprite.body)
                center_body = world.CreateStaticBody(
                    position=(-40, -20),
                    shapes=polygonShape(box=(0.2, 0.2)))

                bird = FlyBird(world, bird_sprites, center_body, "data/hen.png")
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
                world.DestroyJoint(bird.rope)
                world.DestroyJoint(bird.mJoint)
                flag1 = True

            if flag1:
                if (bird.ball_body.position.x - bird.center_body.position.x) ** 2 + (
                        bird.ball_body.position.y - bird.center_body.position.y) ** 2 < 4:
                    world.DestroyJoint(bird.joint)
                    world.DestroyBody(center_body)
                    self.c += 1
                    flag1 = False
                    line = False
                    kill_bird = True

            screen.fill((0, 0, 0, 0))
            util.draw_bodies(world)
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

            world.Step(settings.TIME_STEP, 10, 10)
            all_sprites.update()
            all_sprites.draw(screen)
            bird_sprites.draw(screen)
            pygame.display.flip()
            # if self.c == 3 and died:
            #     NewWindow().run()
            #     self.level = 2
            # clock.tick(TARGET_FPS)


if __name__ == "__main__":
    window = NewWindow2()
    window.run2()
