import math

from pygame.math import Vector2

class Square:
    """
    base class for bouncing objects
    """
    def __init__(self, bounds, width, height, position, velocity, color):
        self.position = position
        self.width = width
        self.height = height
        self.velocity = velocity
        self.bounds = bounds
        self.color = color

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        if self.position.x < 0 or self.position.x > self.bounds[0]: # screen width
            self.velocity.x *= -1
        if self.position.y < 0 or self.position.y > self.bounds[1]: # screen height
            self.velocity.y *= 1
        self.position += self.velocity
        # pass
        
    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.rect(screen, self.color, [int(self.position.x), int(self.position.y), int(self.width), int(self.height)])

# class BouncingBall(Ball):
#     """
#     ball effected by gravity
#     """
   

#     GRAVITY = .1

#     def update(self):  # TODO: Rounding Error
#         # print('called update')
#         self.velocity.y += self.GRAVITY
#         super().update()

# class RainbowBall(Ball):
#     """
#     Ball that changes colors
#     """
#    # TODO:
#     def update(self):
#         r = (self.color[0] + 10) % 256
#         g = (self.color[1] - 5) % 256
#         b = (self.color[2] + 5) % 256
#         self.color = [r, g, b]
#         super().update()

# class BouncingRainbow(RainbowBall, BouncingBall):
#     """
#     Ball that changes color and is affected by gravity
#     """
#     # TODO:
#     pass

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