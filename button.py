import pygame
import sys

pygame.init()

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)

# Шрифт
font = pygame.font.Font(None, 36)


# Класс кнопки
class Button:
    def __init__(self, x, y, width, height, text, window, action=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.action = action
        self.screen = window


    def draw(self):
        # mouse это мышка компьютера, а не наша крыса!!!
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            pygame.draw.rect(self.screen, (200, 200, 200), (self.x, self.y, self.width, self.height))
            if click[0] == 1 and self.action:
                self.action()
        else:
            pygame.draw.rect(self.screen, (150, 150, 150), (self.x, self.y, self.width, self.height))

        text_surface = font.render(self.text, True, black)
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        self.screen.blit(text_surface, text_rect)

