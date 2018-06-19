import math

from pygame.math import Vector2


class Rectangle:
    def __init__(self, velocity, position, width, color, bounds):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.width = width
        # self.height = height

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        # screen width
        if self.position.x < 0 + self.width or self.position.x > self.bounds[0] - self.width:
            self.velocity.x *= -1
        # screen height
        if self.position.y < 0 + self.width or self.position.y > self.bounds[1] - self.width:
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.rect(screen, self.color, pyGame.Rect(
            100, 100, 400, 300))
