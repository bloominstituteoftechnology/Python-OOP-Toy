import math

from pygame.math import Vector2

class Ball:
    """
    base class for bouncing objects
    """
    vel = 
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

class BouncingBall(Ball):
#     """
#     ball effected by gravity
#     """
    def update(self):
        if self.position.x > 0 + self.radius or self.position.x > self.bounds[0] - self.radius:
            self.velocity.y -= 0.3
    
        super().update()
#     # TODO: 

class RainbowBall(Ball):
    def update(self):
        r = (self.color[0] + 3) % 256
        g = (self.color[1] + 2) % 256
        b = (self.color[2] - 1) % 256

        self.color = [r, g, b]
        super().update()
#     """
#     Ball that changes colors
#     """
#     # TODO:

class BouncingRainbow(RainbowBall):
    def update(self):
        if self.position.x > 0 + self.radius or self.position.x > self.bounds[0] - self.radius:
            self.velocity.x -= 0.2
    
        super().update()
#     """
#     Ball that changes color and is affected by gravity
#     """
#     # TODO:

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