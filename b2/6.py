import sys
import pygame
from settings import *
from primitives import Ball, Brick, Bird
from functions import *
import util
import math

# sys.path.append("..")
# from basic_window import run


from Box2D.b2 import world, polygonShape, circleShape, staticBody, dynamicBody
#
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Example_6")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

world = world(gravity=(0, -10))

util.screen = screen
polygonShape.draw = util.my_draw_polygon
circleShape.draw = util.my_draw_circle

util.create_bound(world)


bar_body = world.CreateStaticBody(position=(0, -8), shapes=polygonShape(box=(17, 1.2)))
Brick(all_sprites, bar_body)

brick_body = world.CreateDynamicBody(position=(10, 4))
brick_body.CreatePolygonFixture(box=(3, 10), density=1, friction=0.4)
Brick(all_sprites, brick_body)

brick_body = world.CreateDynamicBody(position=(2, 15))
brick_body.CreatePolygonFixture(box=(15, 2), density=1, friction=0.3)
Brick(all_sprites, brick_body)

brick_body = world.CreateDynamicBody(position=(-7, 4))
brick_body.CreatePolygonFixture(box=(3, 10), density=1, friction=0)
Brick(all_sprites, brick_body)


ball_body = world.CreateDynamicBody(position=(1, 7))
ball_body.CreateCircleFixture(radius=5, density=1, friction=0.3, restitution=0.8)
Ball(all_sprites, ball_body, scale=True)


def create_ball(position):
    ball_body = world.CreateDynamicBody(position=position)
    ball_body.CreateCircleFixture(radius=5, density=1, friction=0.3, restitution=1)
    Ball(all_sprites, ball_body, scale=True)


def create_bir(position):
    ball_body = world.CreateDynamicBody(position=position)
    ball_body.CreateCircleFixture(radius=5, density=1, friction=0.3, restitution=1)
    Bird(all_sprites, ball_body, scale=True)#&


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            create_bir(screen_to_world(event.pos))

    util.screen.fill((0, 0, 0, 0))
    world.Step(TIME_STEP, 10, 10)
    util.draw_bodies(world)
    all_sprites.update()
    all_sprites.draw(util.screen)
    pygame.display.flip()
    clock.tick(TARGET_FPS)
pygame.quit()
