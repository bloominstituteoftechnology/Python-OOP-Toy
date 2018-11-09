import pygame

# import random

# from pygame.math import Vector2
# from pygame import Rect


class Block:
    """
    Base class for square or rectangular object
    """

    def __init__(self, bounds, position, width, height, color):
        # Create a rectangle centered around the x and y
        self.bounds = bounds
        self.position = position
        self.rect = self.set_rectangle(position, width, height)
        self.color = color

    def set_rectangle(self, position, width, height):
        # Creates a rectangle of the given width
        #  and height centered at the x/y coordinates
        return pygame.Rect(
            position.x - (width / 2), position.y - (height / 2), width, height
        )

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.rect.move_ip(0, -5)
                if event.key == pygame.K_DOWN:
                    self.rect.move_ip(0, 5)
                if event.key == pygame.K_LEFT:
                    self.rect.move_ip(-5, 0)
                if event.key == pygame.K_RIGHT:
                    self.rect.move_ip(5, 0)

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)


class RainbowBlock(Block):
    def update(self):
        r = (self.color[0] + 3) % 256
        g = (self.color[1] + 2) % 256
        b = (self.color[2] + 1) % 256

        self.color = [r, g, b]
        super().update()
