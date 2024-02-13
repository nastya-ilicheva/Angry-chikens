from primitives import Ball, Brick
from functions import *
from data import util

from Box2D.b2 import world, polygonShape, circleShape

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Example_6")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

world = world(gravity=(0, -10))

util.screen = screen
polygonShape.draw = util.my_draw_polygon
circleShape.draw = util.my_draw_circle

util.create_bound(world)

bar_body = world.CreateStaticBody(position=(0, 0), shapes=polygonShape(box=(11, 1)))
Brick(all_sprites, bar_body)

brick_body = world.CreateDynamicBody(position=(3, 4))
brick_body.CreatePolygonFixture(box=(1, 2), density=1, friction=0.3)
Ball(all_sprites, brick_body)

brick_body = world.CreateDynamicBody(position=(3, 8))
brick_body.CreatePolygonFixture(box=(1, 2), density=1, friction=0.3)
Brick(all_sprites, bar_body)

brick_body = world.CreateDynamicBody(position=(3, 12))
brick_body.CreatePolygonFixture(box=(1, 2), density=1, friction=0.3)
Brick(all_sprites, bar_body)




def create_ball(position):
    ball_body = world.CreateDynamicBody(position=position)
    ball_body.CreateCircleFixture(radius=5, density=1, friction=0.3, restitution=1)
    Ball(all_sprites, ball_body, scale=True)

#
# create_ball((-3, 7))
#

#


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            create_ball(screen_to_world(event.pos))

    screen.fill((0, 0, 0, 0))
    world.Step(TIME_STEP, 10, 10)
    util.draw_bodies(world)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(TARGET_FPS)
pygame.quit()
