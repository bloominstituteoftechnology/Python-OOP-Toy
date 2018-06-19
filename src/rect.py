import math
import pygame


class Rectangle:
    """base class for rectangles"""

    def __init__(self, top, left, width, height,  color):
        self.color = color
        self.top = top
        self.left = left
        self.height = height
        self.width = width
        self.rectangle = pygame.Rect(
            self.left, self.top, self.width, self.height)

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)

    def update(self):
        pass
