import pygame
from b2.classes import ImageSpriteBody, AnimatedImageSpriteBody


# class Ball(ImageSpriteBody):
#     image = pygame.image.load("data/mouse.png")


import pygame
from b2.classes import ImageSpriteBody, AnimatedImageSpriteBody


class Ball(ImageSpriteBody):
    image = pygame.image.load("data/main_rat.png")


class Brick(ImageSpriteBody):
    image = pygame.image.load("data/kamen.jpg")


class Bird(ImageSpriteBody):
    image = pygame.image.load("data/litle_red_birdpng.png")


class Bird1(AnimatedImageSpriteBody):
    image = pygame.image.load("data/litle_red_bird.png")
