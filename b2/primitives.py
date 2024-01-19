import pygame
from classes import ImageSpriteBody


class Ball(ImageSpriteBody):
    image = pygame.image.load("../data/mouse.png")


class Brick(ImageSpriteBody):
    image = pygame.image.load("../data/stone-wall-64x64.png")
