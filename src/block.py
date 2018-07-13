import pygame
import random

from pygame.math import Vector2
from pygame import Rect

class Block:
    """
    Base class for square or rectangular object
    """
    
    def __init__(self, bounds, position, velocity, width, height, color):
        # Create a rectangle centered around the x and y
        self.bounds = bounds
        self.position = position
        self.velocity = velocity
        self.width = width
        self.height = height
        self.rectangle = self.set_rectangle(position, velocity, width, height)
        self.color = color

    def update(self):
        self.set_rectangle(self.position, self.velocity, self.width, self.height)

    def set_rectangle(self, position, velocity, width, height):
        # Creates a rectangle of the given width and height centered at the x/y coordinates
        x = random.randint(10, 100)
        y = random.randint(10, 100)
        return pygame.Rect(position.x - (width/2),
                           position.y - (height/2),
                                    width,
                                    height)

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)

class RainbowBlock(Block):
    def update(self):
        r = (self.color[0] + 3) % 256
        g = (self.color[1] + 2) % 256
        b = (self.color[2] - 1) % 256

        self.color = [r, g, b]

        super().update()

class KineticBlock(Block):
    def __init__(self, block_list, bounds, position, velocity, width, height, color):
        self.block_list = block_list
        super().__init__(bounds, position, velocity, width, height, color)
    
    def update(self):
        for block in self.block_list:
            if block == self:
                continue

            else:
                distance = block.position.distance_to(self.position)
                sumwidth = self.width + block.width

                if distance < sumwidth:
                    print("Block collision!")
        super().update()