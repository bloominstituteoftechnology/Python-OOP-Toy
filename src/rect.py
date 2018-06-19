import math

from pygame.math import Vector2


class Rect:
    """
    base class for bouncing objects
    """

    def __init__(self, bounds, position, velocity, color, width):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.width = width

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        # screen width
        if self.position.x < 0 + self.width or self.position.x > self.bounds[1] - self.width:
            self.velocity.x *= -1
        # screen height
        if self.position.y < 0 + self.width or self.position.y > self.bounds[0] - self.width:
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.rect(screen, self.color, [
                         self.position.y, self.position.x, self.width, self.width])


class BouncingRect(Rect):
    """
    ball effected by gravity
    """
    GRAVITY = 5.5

    def update(self):
        # This function will override the update in Ball()
        print('called update in BouncingRect')
        self.velocity.y += self.GRAVITY
        # Now that you've done your class specific stuff, call your parents
        # update function
        super().update()


class RainbowRect(Rect):
    """
    Rect that changes colors
    """

    def update(self):
        r = (self.color[0] + 1) % 256
        g = (self.color[1] - 2) % 256
        b = (self.color[2] + 5) % 256
        self.color = [r, g, b]
        super().update()


class BouncingRainbow(BouncingRect, RainbowRect):
    """
    Rect that changes color and is affected by gravity
    """
    pass
