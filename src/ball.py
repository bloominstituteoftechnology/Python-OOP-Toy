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
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius: 
            self.velocity.x *= -1  # screen width
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius:
            self.velocity.y *= -1  # screen height
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)


class BouncingBall(Ball):
    """
    ball effected by gravity
    """

    def __init__(self, bounds, position, velocity, color, radius):
        super().__init__(bounds, position, velocity, color, radius)
        self.max_velocity_y = math.fabs(velocity.y) + 10
        self.friction = 1

    def update(self):
        # if falling increase v until it hits max else decrease v until it hits 0
        if self.velocity.y >= 0:  # 
            if self.velocity.y < self.max_velocity_y:
                self.velocity.y += 0.25
        else:
            if self.velocity.y != 0:
                self.velocity.y += 0.25
                # self.velocity.y += (0.25 * self.friction)
        
        # if ball hits the ground increase friction
        # TODO how to make it come to a complete stop?
        # if self.position.y > self.bounds[1] - self.radius:
        #     self.friction += 0.25

        super().update()


class RainbowBall(Ball):
    """
    Ball that changes colors
    """

    def update(self):
        r = (self.color[0] + 1) % 255
        g = (self.color[1] + 5) % 255
        b = (self.color[2] + 10) % 255
        self.color = [r, g, b]

        super().update()
    
# class BouncingRainbow(???):
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
