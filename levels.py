from b2.primitives import *
from Box2D.b2 import world, polygonShape, circleShape
from catapult import FlyBird


def level_1(world, all_sprites, bird_sprites):
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
        shapes=polygonShape(box=(0.2, 0.2)))

    bird = FlyBird(world, bird_sprites, center_body, "data/litle_red_bird.png")
    return center_body, bird, RAT


def level_2(world, all_sprites, bird_sprites):
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

    bird = FlyBird(world, bird_sprites, center_body, "data/hen.png")
    return center_body, bird, RAT


def level_3(world, all_sprites, bird_sprites):
    bar_body = world.CreateStaticBody(position=(29, -28), shapes=polygonShape(box=(30, 1)))
    Brick(all_sprites, bar_body)  # пол

    brick_body = world.CreateDynamicBody(position=(21, -20))
    brick_body.CreatePolygonFixture(box=(5.5, 9), density=9, friction=1)
    Brick(all_sprites, brick_body)  # правая стена

    brick_body = world.CreateDynamicBody(position=(30, -20))
    brick_body.CreatePolygonFixture(box=(10, 9), density=5, friction=0.8)
    Brick(all_sprites, brick_body)  # левая стена

    brick_body = world.CreateDynamicBody(position=(28, -15))
    brick_body.CreatePolygonFixture(box=(2, 21), density=10, friction=1)
    Brick(all_sprites, brick_body)  # крыша
    #
    ball_body = world.CreateDynamicBody(position=(29, -8))
    ball_body.CreateCircleFixture(radius=6, density=15, friction=1, restitution=0.8)
    RAT = Ball(all_sprites, ball_body, scale=True)

    center_body = world.CreateStaticBody(
        position=(-40, -20),
        shapes=polygonShape(box=(0.2, 0.2)))

    bird = FlyBird(world, bird_sprites, center_body, "data/red_circle.png")
    return center_body, bird, RAT
