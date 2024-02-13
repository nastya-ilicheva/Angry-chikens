from primitives import Ball, Brick
from functions import *
from data import util

from Box2D.b2 import world, polygonShape, circleShape

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Example_5")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

world = world(gravity=(0, -10))

util.create_bound(world)

bar_body = world.CreateStaticBody(position=(0, 0), shapes=polygonShape(box=(11, 1)), angle=-0.2)
Brick(all_sprites, bar_body)


def create_ball(position):
    ball_body = world.CreateDynamicBody(position=position)
    ball_body.CreateCircleFixture(radius=3, density=1, friction=0.3, restitution=1)
    Ball(all_sprites, ball_body, scale=True)


create_ball((-3, 7))

brick_body = world.CreateDynamicBody(position=(3, 15), angle=0.2)
brick_body.CreatePolygonFixture(box=(4, 4), density=1, friction=0.3, restitution=1)
Brick(all_sprites, brick_body)

util.screen = screen
polygonShape.draw = util.my_draw_polygon
circleShape.draw = util.my_draw_circle

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
