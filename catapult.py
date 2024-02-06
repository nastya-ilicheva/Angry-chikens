import pygame

# from b2.catapult import ball_body
from b2.settings import *
from b2.primitives import Ball, Brick, Bird, Bird1
# from b2.functions import *
# import b2.util
from math import sin

from Box2D.b2 import world, polygonShape, circleShape, staticBody, dynamicBody
from Box2D import b2Color, b2MouseJointDef, b2RopeJointDef

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Catapult")
# clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


# world = world(gravity=(0, -25))

# util.screen = screen
# polygonShape.draw = util.my_draw_polygon
# circleShape.draw = util.my_draw_circle


class FlyBird:

    def __init__(self, world, sprite_group, center_body):
        self.ball_body = world.CreateDynamicBody(position=(-40, -20))
        self.ball_body.CreateCircleFixture(radius=3, density=10, friction=0.5, restitution=0)

        self.center_body = center_body

        self.sprite = Bird1(sprite_group, self.ball_body, img=pygame.image.load("data/litle_red_bird.png"), columns=4,
                            rows=1, scale=True)

        self.joint = world.CreateMotorJoint(bodyA=self.ball_body, bodyB=self.center_body, maxForce=1000,
                                            maxTorque=1000000)

        self.mJoint = world.CreateMouseJoint(bodyA=self.center_body,
                                             bodyB=self.ball_body,
                                             target=self.ball_body.position,
                                             maxForce=50000.0)

        self.rope = world.CreateJoint(b2RopeJointDef(
            bodyA=self.ball_body,
            bodyB=self.center_body,
            maxLength=20,
            localAnchorA=(0, 0),
            localAnchorB=(0, 0)))

    def create_ball(position):
        ball_body = world.CreateDynamicBody(position=position)
        ball_body.CreateCircleFixture(radius=5, density=1, friction=0.3, restitution=1)
        Ball(all_sprites, ball_body, scale=True)


