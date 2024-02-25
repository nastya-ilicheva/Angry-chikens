from b2.primitives import *
from Box2D.b2 import world, polygonShape, circleShape
from bird import FlyBird


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
    rat = Ball(all_sprites, ball_body, scale=True)

    center_body = world.CreateStaticBody(
        position=(-40, -20),
        shapes=polygonShape(box=(0.2, 0.2)))

    bird = FlyBird(world, bird_sprites, center_body, "data/litle_red_bird.png")
    return center_body, bird, rat, 1, "data/litle_red_bird.png"


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
    rat = Ball(all_sprites, ball_body, scale=True)

    center_body = world.CreateStaticBody(
        position=(-40, -20),
        shapes=polygonShape(box=(0.5, 0.5)))

    bird = FlyBird(world, bird_sprites, center_body, "data/hen.png")
    return center_body, bird, rat, 1, "data/hen.png"


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
    rat = Ball(all_sprites, ball_body, scale=True)

    center_body = world.CreateStaticBody(
        position=(-40, -20),
        shapes=polygonShape(box=(0.2, 0.2)))

    bird = FlyBird(world, bird_sprites, center_body, "data/yellow_hen.png")
    return center_body, bird, rat, 3, "data/yellow_hen.png"


def level_4(world, all_sprites, bird_sprites):
    bar_body = world.CreateStaticBody(position=(35, -27), shapes=polygonShape(box=(33, 1)))
    Brick(all_sprites, bar_body)  # пол

    brick_body = world.CreateDynamicBody(position=(27, -24))
    brick_body.CreatePolygonFixture(box=(15, 5), density=20, friction=8)
    Brick(all_sprites, brick_body)  # правая стена

    brick_body = world.CreateDynamicBody(position=(30, -20))
    brick_body.CreatePolygonFixture(box=(33, 1.2), density=10, friction=8)
    Brick(all_sprites, brick_body)  # крыша
    #
    ball_body = world.CreateDynamicBody(position=(15, -26))
    ball_body.CreateCircleFixture(radius=5, density=15, friction=1.75, restitution=1.25)
    rat = Ball(all_sprites, ball_body, scale=True)

    center_body = world.CreateStaticBody(position=(-40, -20), shapes=polygonShape(box=(0.2, 0.2)))

    bird = FlyBird(world, bird_sprites, center_body, "data/blue_hen.png")
    return center_body, bird, rat, 3, "data/blue_hen.png"


def level_5(world, all_sprites, bird_sprites):
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
    rat = Ball(all_sprites, ball_body, scale=True)

    center_body = world.CreateStaticBody(
        position=(-40, -20),
        shapes=polygonShape(box=(0.2, 0.2)))

    bird = FlyBird(world, bird_sprites, center_body, "data/blue_hen.png")
    return center_body, bird, rat, 3, "data/blue_hen.png"
