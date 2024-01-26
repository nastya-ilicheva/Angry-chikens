import pygame
import sys
from rat import Rat
from catapult import Catapult

from Box2D.b2 import world, polygonShape, circleShape, staticBody, dynamicBody
from b2 import util, primitives, settings, classes, functions
from b2.primitives import *

pygame.init()


class NewWindow:
    def __init__(self):
        self.fon = pygame.image.load("data/snow.jpg")

    def run(self):
        self.fon = pygame.transform.scale(self.fon, (1300, 750))
        self.width, self.height = self.fon.get_width(), self.fon.get_height()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("New Window")

        MYEVENTTYPE = pygame.USEREVENT + 1
        pygame.time.set_timer(MYEVENTTYPE, 4)

        all_sprites = pygame.sprite.Group()

        util.screen = screen

        bar_body = world.CreateStaticBody(position=(29, -28), shapes=polygonShape(box=(20, 1)))
        Brick(all_sprites, bar_body)  # пол

        brick_body = world.CreateDynamicBody(position=(19, -20))
        brick_body.CreatePolygonFixture(box=(4, 12), density=1, friction=0.4)
        Brick(all_sprites, brick_body)  # правая стена

        brick_body = world.CreateDynamicBody(position=(37, -20))
        brick_body.CreatePolygonFixture(box=(4, 12), density=1, friction=0.3)
        Brick(all_sprites, brick_body)  # левая стена

        brick_body = world.CreateDynamicBody(position=(28, -15))
        brick_body.CreatePolygonFixture(box=(21, 2), density=1, friction=0.4)
        Brick(all_sprites, brick_body)  # крыша
        #
        ball_body = world.CreateDynamicBody(position=(29, -21))
        ball_body.CreateCircleFixture(radius=5, density=1, friction=0.3, restitution=0.8)
        Ball(all_sprites, ball_body, scale=True)  # крысяндра в крепости

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MYEVENTTYPE:
                    all_sprites.update()

            screen.blit(self.fon, (0, 0))

            # util.screen.fill((0, 0, 0, 0))
            world.Step(settings.TIME_STEP, 10, 10)

            all_sprites.draw(screen)
            pygame.display.flip()


if __name__ == "__main__":
    world = world(gravity=(0, -0.5))
    window = NewWindow()
    window.run()