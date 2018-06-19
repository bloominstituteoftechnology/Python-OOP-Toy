import math

from pygame.math import Vector2


class Rectangle:
    def __init__(self, bounds, position, velocity, color, width, length):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.width = width
        self.length = length

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        # screen width
        if self.position.x < 0 + self.width or self.position.x > self.bounds[0] - self.width:
            self.velocity.x *= -1
        # screen height
        if self.position.y < 0 + self.length or self.position.y > self.bounds[1] - self.length:
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.rect(screen, self.color, (int(self.position.x), int(
            self.position.y), int(self.width), int(self.length)))
