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
#     ball effected by gravity
#     """
#     # TODO: 

class BouncingBall(Ball):

    def update(self):

        if self.velocity.y < -0.5:
            self.velocity.y -= (0.098 * self.velocity.y)
        elif self.velocity.y > 0:
            if self.velocity.y < 30:
                self.velocity.y += (0.098 * self.velocity.y)
            else:
                self.velocity.y = 30
        else:
            self.velocity.y = 1

        super().update()

# class RainbowBall(???):
#     """
#     Ball that changes colors
#     """
#     # TODO:

class RainbowBall(Ball):

    def update(self):
        r = (self.color[0] + 3) % 256
        g = (self.color[1] + 2) % 256
        b = (self.color[2] - 1) % 256

        self.color = [r, g, b]

        # call the superclass {Block} update()
        super().update()

# class BouncingRainbow(???):
#     """
#     Ball that changes color and is affected by gravity
#     """
#     # TODO:

class BouncingRainbow(Ball):

    def update(self):
        if self.velocity.y < -0.5:
            self.velocity.y -= (0.098 * self.velocity.y)
        elif self.velocity.y > 0:
            if self.velocity.y < 30:
                self.velocity.y += (0.098 * self.velocity.y)
            else:
                self.velocity.y = 30
        else:
            self.velocity.y = 1

        r = (self.color[0] + 3) % 256
        g = (self.color[1] + 2) % 256
        b = (self.color[2] - 1) % 256

        self.color = [r, g, b]

        # call the superclass {Block} update()
        super().update()

# STRETCH GOALS:

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