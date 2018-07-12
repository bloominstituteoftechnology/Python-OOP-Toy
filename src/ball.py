import math
import numpy

from pygame.math import Vector2
from decimal import *
from random import *
from numpy import *

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


class RainbowBall(Ball):
    """
    Ball that changes colors
    """

    def __init__(self, bounds, position, velocity, color, radius):
        super().__init__(bounds, position, velocity, color, radius)

    def update(self):
        self.color[0] = self.position.x % 255
        self.color[1] = self.position.y % 255
        self.color[2] = (self.position.x - self.position.y) % 255
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius: # screen width
            self.velocity.x *= -1
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius: # screen height
            self.velocity.y *= -1
        self.position += self.velocity


class BouncingRainbow(Ball):
    """
    Ball that changes color and is affected by gravity
    """
    def __init__(self, bounds, position, velocity, color, radius):
        #big: f(100 * x = 0 , ((100 - 20) / 100) * -1 = -0.2
        #small: f(0.1) = 1 , ((100 - 10) / 100) * -1 = 
        self.g = -1 * ((100 - radius) / 100)
        self.friction = -1
        super().__init__(bounds, position, velocity, color, radius)

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges

        self.color[0] = self.position.x % 255
        self.color[1] = self.position.y % 255
        self.color[2] = (self.velocity.x - int(self.velocity.y)) % 255

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


## STRETCH

class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    def __init__(self, object_list, bounds, position, velocity, color, radius):
        self.object_list = object_list
        super().__init__(bounds, position, velocity, color, radius)

    def update(self):
        for obj in self.object_list:

            if obj == self:
                continue

            distance = obj.position.distance_to(self.position)

            sumr = self.radius + obj.radius

            if distance < sumr:
                print("Collision!")
                v1 = self.velocity.x
                v2 = obj.velocity.x
                m1 = self.radius
                m2 = obj.radius
                p1 = self.position.x
                p2 = obj.position.x

                # self.velocity.x = ( (v1*(m1-m2))+(2*m2*v2) ) / (m1 + m2)
                # obj.velocity.x = (( (v1*(m1-m2))+(2*m2*v2) ) / (m1 + m2)) * -1
                
                # self.velocity.x = v1  -  ((2*m2) / (m1+m2))  *  (numpy.dot( v1-v2 , p1-p2 ) / (numpy.linalg.norm(p1-p2)**2))  *  (p1 - p2)


                v1 = self.velocity
                v2 = obj.velocity
                m1 = self.radius
                m2 = obj.radius
                p1 = self.position
                p2 = obj.position

                self.velocity = v1  -  ((2*m2) / (m1+m2))  *  (numpy.dot( v1-v2 , p1-p2 ) / (numpy.linalg.norm(p1-p2)**2))  *  (p1 - p2)
                obj.velocity = v2  -  ((2*m1) / (m1+m2))  *  (numpy.dot( v2-v1 , p2-p1 ) / (numpy.linalg.norm(p2-p1)**2))  *  (p2 - p1)


                # v1 = self.velocity.y
                # v2 = obj.velocity.y
                # m1 = self.radius
                # m2 = obj.radius
                # p1 = self.position.y
                # p2 = obj.position.y

                # self.velocity.y = ( (v1*(m1-m2))+(2*m2*v2) ) / (m1 + m2)
                # obj.velocity.y = (( (v1*(m1-m2))+(2*m2*v2) ) / (m1 + m2)) * -1
                
                # self.velocity.y = v1  -  ((2*m2) / (m1+m2))  *  (numpy.dot( v1-v2 , p1-p2 ) / (numpy.linalg.norm(p1-p2)**2))  *  (p1 - p2)




        super().update()

# class KineticBouncing(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """
    

# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """