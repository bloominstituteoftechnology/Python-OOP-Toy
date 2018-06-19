import math

from pygame.math import Vector2


class Rectangle:
    def __init__(self, bounds, position, length, width, color, velocity):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.length = length
        self.width = width

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        # screen width
        if self.position.x < 0 + self.length + self.width or self.position.x > self.bounds[0] - self.length - self.width:
            self.velocity.x *= -1
        # screen height
        if self.position.y < 0 + self.length + self.width or self.position.y > self.bounds[1] - self.length - self.width:
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(
            self.position.x), int(self.position.y)], self.length)
