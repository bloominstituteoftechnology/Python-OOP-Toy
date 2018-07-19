import pygame
import random

from pygame.math import Vector2
from pygame import Rect


class Block:
    """
    Base class for square or rectangular object
    """

    def __init__(self, bounds, position, width, height, color):
        # Create a rectangle centered around the x and y
        self.bounds = bounds
        self.position = position
        self.rectangle = self.set_rectangle(position, width, height)
        self.color = color

    def update(self):
        # TODO:  Add base functionality
        pass

    def set_rectangle(self, position, width, height):
        # Creates a rectangle of the given width and height centered at the x/y coordinates
        return pygame.Rect(
            position.x - (width / 2), position.y - (height / 2), width, height
        )

    def draw(self, screen, pygame):
        pygame.draw.rect(screen, self.color, self.rectangle)


class AlsoABlock(Block):
    # This class inherits from Block and has no other code, so it is identical!
    pass


class RainbowBlock(Block):
    # This class overrides the update method to add new functionality.
    def update(self):
        r = (self.color[0] + 3) % 256
        g = (self.color[1] + 2) % 256
        b = (self.color[2] - 1) % 256
        self.color = [r, g, b]
        super().update()


class PulsingBlock(Block):
    # This class overrides the init function to add new variables, before calling the parent
    # init function.  It uses the extra variables in an override of update to add new
    # functionality.
    # This rectangle increases in size by pulse_rate, until it reaches pulse_size, then
    # it contracts to the original size
    def __init__(self, pulse_size, pulse_rate, bounds, position, width, height, color):
        self.base_width = width
        self.base_height = height
        self.width = width
        self.height = height
        self.pulse_size = pulse_size
        self.pulse_rate = pulse_rate
        self.is_expanding = True
        super().__init__(bounds, position, width, height, color)

    def update(self):
        self.width += self.pulse_rate
        self.height += self.pulse_rate
        self.rectangle = self.set_rectangle(self.position, self.width, self.height)
        if (
            self.width >= self.base_width + self.pulse_size
            or self.width <= self.base_width
        ):
            self.pulse_rate *= -1
        super().update()


class PulsingRainbow(RainbowBlock, PulsingBlock):
    # Multiple inheritance
    pass
