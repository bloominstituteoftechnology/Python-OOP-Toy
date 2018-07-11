import math

from pygame.math import Vector2
from decimal import *
from random import *

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

class BouncingBall(Ball):
    """
    ball effected by gravity
    """
    def __init__(self, bounds, position, velocity, color, radius):
        #big: f(100 * x = 0 , ((100 - 20) / 100) * -1 = -0.2
        #small: f(0.1) = 1 , ((100 - 10) / 100) * -1 = 
        self.g = -1 * ((100 - radius) / 100)
        self.friction = -1
        super().__init__(bounds, position, velocity, color, radius)

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges

        # gravity affecting acceleration
        if self.g < 0.2 + self.radius:
            self.velocity.y += 0.2
        
        # reduces x direction velocity with friction
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius: # screen width
            #self.velocity.x *= -1
            if self.friction < -1.3877787807814457e-16:
                self.friction += 0.1
            else:
                self.friction = 0
            self.velocity.x *= self.friction

        # reduces y direction velocity with
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius: # screen height
            if self.friction < -1.3877787807814457e-16:
                self.friction += 0.1
            else:
                self.velocity.x = 0
            
            if self.g < 0.2 + self.radius:
                self.velocity.y = self.velocity.y * self.g

            if self.g < -1.3877787807814457e-16:
                self.g += 0.1

                
        if self.position.y > self.bounds[1] - self.radius:
            self.position.y = self.bounds[1] - self.radius
        
        self.position += self.velocity

    # TODO: 

class RainbowBall(Ball):
    """
    Ball that changes colors
    """

    def __init__(self, bounds, position, velocity, color, radius):
        super().__init__(bounds, position, velocity, color, radius)

    def update(self):
        self.color = [int(random() * 255), int(random() * 255), int(random() * 255)]
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius: # screen width
            self.velocity.x *= -1
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius: # screen height
            self.velocity.y *= -1
        self.position += self.velocity


    # TODO:

# class BouncingRainbow(???):
#     """
#     Ball that changes color and is affected by gravity
#     """
#     # TODO:

## STRETCH

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