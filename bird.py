import pygame

# from b2.catapult import ball_body
from b2.settings import *
from b2.primitives import Ball, Brick, Bird, Bird1
# from b2.functions import *
# import b2.util
from math import sin

from Box2D.b2 import world, polygonShape, circleShape, staticBody, dynamicBody
from Box2D import b2Color, b2MouseJointDef, b2RopeJointDef

all_sprites = pygame.sprite.Group()


class FlyBird:

    def __init__(self, world, sprite_group, center_body, image):
        self.ball_body = world.CreateDynamicBody(position=(-40, -20))
        self.ball_body.CreateCircleFixture(radius=3, density=10, friction=0.5, restitution=0)

        self.center_body = center_body

        self.sprite = None

        self.joint = world.CreateMotorJoint(bodyA=self.ball_body, bodyB=self.center_body, maxForce=1000,
                                            maxTorque=1000000)

        self.mJoint = world.CreateMouseJoint(bodyA=self.center_body,
                                             bodyB=self.ball_body,
                                             target=self.ball_body.position,
                                             maxForce=50000.0)

        self.rope = world.CreateJoint(b2RopeJointDef(
            bodyA=self.ball_body,
            bodyB=self.center_body,
            maxLength=15,
            localAnchorA=(0, 0),
            localAnchorB=(0, 0)))

        self.sprite = Bird1(sprite_group, self.ball_body, img=pygame.image.load(image), columns=4,
                            rows=1, scale=True)

    def create_ball(position):
        ball_body = world.CreateDynamicBody(position=position)
        ball_body.CreateCircleFixture(radius=5, density=1, friction=0.3, restitution=1)
        Ball(all_sprites, ball_body, scale=True)
