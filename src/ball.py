import math

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

# ***PERSONAL NOTE:looks like this block is regarding movement and screen dimension***
    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius: # screen width
            self.velocity.x *= -1
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius: # screen height
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)



# class BouncingBall(???):
#     """
#     ball effected by gravity ***PERSONAL NOTE: implement effect ball by gravity***
#     """
#     # TODO: 
"""class BouncingBall:
    def__init__(self, gravity):
        self.gravity = gravity"""

# class RainbowBall(???):
#     """
#     Ball that changes colors ***PERSONAL NOTE: implement ball change colors***
#     """
#     # TODO:
class RainbowBall(Ball):

def update(self):
    r = (self.colors[0] +3) %256
    g = (self.colors[0] +3) %256
    b = (self.colors[0] +3) %256

    self.color = [r, g, b]
    super().update()


# class BouncingRainbow(???):
#     """
#     Ball that changes color and is affected by gravity ***PERSONAL NOTE: use class BouncingBall and class RainbowBall***
#     """
#     # TODO:
"""lass BoumcingRainbow:
    def__init__(self, gravity, colors):
        self.gravity = gravity
        self.colors = colors"""

# STRETCH GOALS after this line

# class KineticBall(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     """
#     # TODO:
"""class KineticBall:
    def__init__(self, elastic, circle, collision):
        self.elastic = elastic
        self.circle = circle
        self.collision = collision"""

# class KineticBouncing(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """
"""class KineticBouncing:
    def__init__(self, simple, elastic, circle, collision):
        self.simple = simple
        self.elastic = elastic
        self.circle = circle
        self.collision = collision"""
    

# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """
"""class AllTheThings:
    def__init__(self, gravity, colors, simple, elastic, circle, collision):"""