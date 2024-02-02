import pygame
import sys
import asyncio

from b2.functions import screen_to_world
from rat import Rat
# from catapult import Catapult
# from Box2D.b2 import world as box2d_world, polygonShape, circleShape, staticBody, dynamicBody
from Box2D.b2 import world, polygonShape, circleShape, staticBody, dynamicBody
from Box2D import b2RopeJointDef
from b2 import util, primitives, settings, classes, functions
from b2.primitives import *

from catapult import FlyBird

pygame.init()


class NewWindow:
    def __init__(self):
        self.fon = pygame.image.load("data/snow.jpg")
        self.all_sprites = pygame.sprite.Group()  # создаем группу спрайтов для всех спрайтов

        self.bricks = []  # список для хранения ссылок на спрайты

        bar_body = world.CreateStaticBody(position=(29, -28), shapes=polygonShape(box=(20, 1)))
        brick_sprite = Brick(self.all_sprites, bar_body)
        self.bricks.append(brick_sprite)  # сохраняем ссылку на спрайт

    # async def create_bird(self):
    #     await asyncio.sleep(3)
    #     bird = FlyBird()
    #     bird.start(world)
    #     Bird(self.all_sprites, bird.ball_body, scale=True)

    def run(self):
        self.fon = pygame.transform.scale(self.fon, (1300, 750))
        self.width, self.height = self.fon.get_width(), self.fon.get_height()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("New Window")

        MYEVENTTYPE = pygame.USEREVENT + 1
        pygame.time.set_timer(MYEVENTTYPE, 4)

        all_sprites = pygame.sprite.Group()

        util.screen = screen
        polygonShape.draw = util.my_draw_polygon
        circleShape.draw = util.my_draw_circle

        bar_body = world.CreateStaticBody(position=(29, -28), shapes=polygonShape(box=(20, 1)))
        Brick(all_sprites, bar_body)  # пол

        brick_body = world.CreateDynamicBody(position=(19, -20))
        brick_body.CreatePolygonFixture(box=(4, 12), density=1, friction=0.6)
        Brick(all_sprites, brick_body)  # правая стена

        brick_body = world.CreateDynamicBody(position=(37, -20))
        brick_body.CreatePolygonFixture(box=(4, 12), density=1, friction=0.6)
        Brick(all_sprites, brick_body)  # левая стена

        brick_body = world.CreateDynamicBody(position=(28, -15))
        brick_body.CreatePolygonFixture(box=(21, 2), density=1, friction=0.6)
        Brick(all_sprites, brick_body)  # крыша
        #
        ball_body = world.CreateDynamicBody(position=(29, -21))
        ball_body.CreateCircleFixture(radius=6, density=0.3, friction=0.1, restitution=1)
        Ball(all_sprites, ball_body, scale=True)  # крысяндра в крепости

        RAT = Ball(all_sprites, ball_body, scale=True)

        running = True
        died = False

        def create_ball(position):
            ball_body = world.CreateDynamicBody(position=position)
            ball_body.CreateCircleFixture(radius=5, density=1, friction=0.3, restitution=1)
            Ball(all_sprites, ball_body, scale=True)

        bird = FlyBird()
        bird.start(world)
        Bird(all_sprites, bird.ball_body, scale=True)

        flag = True
        flag1 = True

        running = True
        moving = False

        pygame.mixer.music.load('data/chiken_music.mp3')
        pygame.mixer.music.play()

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for contact in world.contacts:
                    fixture_a = contact.fixtureA
                    fixture_b = contact.fixtureB

                    if (fixture_a.body == brick_body and fixture_b.body == RAT.body) or (
                            fixture_a.body == RAT.body and fixture_b.body == brick_body):
                        world.DestroyBody(RAT.body)
                        died = True
                        RAT.kill()

                if event.type == MYEVENTTYPE:
                    all_sprites.update()

                # elif event.type == pygame.MOUSEBUTTONDOWN:
                #     if event.button == 1:
                #         click_pos = pygame.mouse.get_pos()
                #         ball_body = world.CreateDynamicBody(position=(click_pos[0] // 5, click_pos[1] // 2))
                #         ball_body.CreateCircleFixture(radius=5, density=1, friction=0.3, restitution=0.8)
                #         Bird(all_sprites, ball_body, scale=True)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    moving = True
                    print(1)
                if event.type == pygame.MOUSEMOTION:
                    if moving:
                        bird.mJoint.target = screen_to_world(pygame.mouse.get_pos())
                        print(2)
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    moving = False
                    print(3)
                    world.DestroyBody(bird.center_body1)
                    world.DestroyJoint(bird.rope)
                    world.DestroyJoint(bird.mJoint)
                    print(4)

            screen.blit(self.fon, (0, 0))
            world.Step(settings.TIME_STEP, 10, 10)

            all_sprites.draw(screen)
            if died:
                RAT.kill()  # удаление спрайта brick_body из группы спрайтов
                died = False  # сброс флага died обратно в False, чтобы установить возможность будущих проверок столкновений

            pygame.display.flip()

            # catapult
            if flag1:
                print(bird.ball_body.position, bird.center_body.position)
                if (bird.ball_body.position.x - bird.center_body.position.x) ** 2 + ( bird.ball_body.position.y - bird.center_body.position.y) ** 2 < 4:
                    print(5)
                    world.DestroyJoint(bird.joint)
                    world.DestroyBody(bird.center_body)
                    flag1 = False

                    # asyncio.run(self.create_bird())

                    # bird1 = FlyBird()
                    # bird1.start(world)
                    # Bird(all_sprites, bird1.ball_body, scale=True)

            # screen.fill((0, 0, 0, 0))
            # world.Step(TIME_STEP, 10, 10)
            util.draw_bodies(world)
            # all_sprites.update()
            # all_sprites.draw(screen)
            # pygame.display.flip()
            # clock.tick(TARGET_FPS)


if __name__ == "__main__":
    world = world(gravity=(0, -0.5))
    window = NewWindow()
    window.run()
