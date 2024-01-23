import pygame
from settings import *
from primitives import Ball, Brick
from functions import *
import util
from math import sin

from Box2D.b2 import world, polygonShape, circleShape, staticBody, dynamicBody
from Box2D import b2Color, b2MouseJointDef

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catapult")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

world = world(gravity=(0, 0))

util.screen = screen
polygonShape.draw = util.my_draw_polygon
circleShape.draw = util.my_draw_circle

# util.create_bound(world)
#
#
# bar_body = world.CreateStaticBody(position=(0, -8), shapes=polygonShape(box=(17, 1.2)))
# Brick(all_sprites, bar_body) #нужен brick_body но на все
#
# brick_body = world.CreateDynamicBody(position=(10, 4))
# brick_body.CreatePolygonFixture(box=(3, 10), density=1, friction=0.4)
# Ball(all_sprites, brick_body)
#
# brick_body = world.CreateDynamicBody(position=(2, 15))
# brick_body.CreatePolygonFixture(box=(15, 2), density=1, friction=0.3)
# Brick(all_sprites, brick_body)
#
# brick_body = world.CreateDynamicBody(position=(-7, 4))
# brick_body.CreatePolygonFixture(box=(3, 10), density=1, friction=0)
# Brick(all_sprites, brick_body)


ball_body = world.CreateDynamicBody(position=(-15, -15))
ball_body.CreateCircleFixture(radius=5, density=1, friction=0.3, restitution=0)

Ball(all_sprites, ball_body, scale=True)

center_body = world.CreateStaticBody(
        position=(0, 0),
        shapes=polygonShape(box=(1, 1))
    )
center_body1 = world.CreateStaticBody(position=(0, 0))
center_body1.CreateCircleFixture(radius=3, density=1, friction=0.3)

joint = world.CreateMotorJoint(bodyA=ball_body, bodyB=center_body,
                                                 maxForce=10000, maxTorque=1000)

# md = b2MouseJointDef(, maxForce = 3000)

mJoint = world.CreateMouseJoint(bodyA = center_body, bodyB = ball_body, target=(10,0))


def create_ball(position):
    ball_body = world.CreateDynamicBody(position=position)
    ball_body.CreateCircleFixture(radius=5, density=1, friction=0.3, restitution=1)
    Ball(all_sprites, ball_body, scale=True)


def MouseDown(self, p):
    """
    Indicates that there was a left click at point p (world coordinates)
    """
    if self.mouseJoint is not None:
        return

    # Create a mouse joint on the selected body (assuming it's dynamic)
    # Make a small box.
    aabb = b2AABB(lowerBound=p - (0.001, 0.001),
                  upperBound=p + (0.001, 0.001))

    # Query the world for overlapping shapes.
    query = fwQueryCallback(p)
    self.world.QueryAABB(query, aabb)

    if query.fixture:
        body = query.fixture.body
        # A body was selected, create the mouse joint
        self.mouseJoint = self.world.CreateMouseJoint(
            bodyA=self.groundbody,
            bodyB=body,
            target=p,
            maxForce=1000.0 * body.mass)
        body.awake = True

def MouseUp(self, p):
    """
    Left mouse button up.
    """
    if self.mouseJoint:
        self.world.DestroyJoint(self.mouseJoint)
        self.mouseJoint = None

    if self.bombSpawning:
        self.CompleteBombSpawn(p)

def MouseMove(self, p):
    """
    Mouse moved to point p, in world coordinates.
    """
    self.mouseWorld = p
    if self.mouseJoint:
        self.mouseJoint.target = p



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            world.DestroyBody(center_body1)

    screen.fill((0, 0, 0, 0))
    world.Step(TIME_STEP, 10, 10)
    util.draw_bodies(world)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(TARGET_FPS)
pygame.quit()
