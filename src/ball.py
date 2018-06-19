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
        pygame.draw.rect(screen, self.color, (200,150,100,50))
class BouncingBall(Ball):
    """
    ball effected by gravity
    """
    GRAVITY = .1

    def update(self): #Todo: Fix rounding error that makes it bounce higher
        #This function will override the update in the toy
        # print('called update in BouncingBall')
        self.velocity.y += self.GRAVITY
        #Now that you've done your class specific studd, call your parent's update function
        super().update()
        #this could be withouth the underscores too


class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    def update(self):
        r = (self.color[0] + 10) % 256
        g = (self.color[1] - 5) % 256
        b = (self.color[2] + 5) %256
        self.color = [r,g,b]
        super().update()

class BouncingRainbow(BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    pass

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