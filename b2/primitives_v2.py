import pygame
from b2.classes import ImageSpriteBody


class Ball(ImageSpriteBody):
    image = pygame.image.load("../data/mouse.png")


class Brick(ImageSpriteBody):
    image = pygame.image.load("../data/kamen.jpg")


class Bird(ImageSpriteBody):
    image = pygame.image.load("../data/one_bird.png")
