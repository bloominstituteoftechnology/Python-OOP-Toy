import math
import random

from pygame.math import Vector2


class Ball:
    """
    base class for bouncing objects
    """

    def __init__(self, bounds, position, velocity, color, radius):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.radius = radius

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        # screen width
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius:
            self.velocity.x *= -1
        # screen height
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius:
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(
            self.position.x), int(self.position.y)], self.radius)


class BouncingBall(Ball):
    """
    ball effected by gravity
    """
    # TODO:
    Gravity = 0.1

    def update(self):
        self.velocity.y += self.Gravity

        # call parent function
        super().update()


class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    # TODO:

    def update(self):
        self.color[0] = random.randint(0, 255)
        self.color[1] = random.randint(0, 255)
        self.color[2] = random.randint(0, 255)

        super().update()


class BouncingRainbow(BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    # TODO:

# class KineticBall(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     """
#     # TODO:

# class KineticBouncing(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """


# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """
