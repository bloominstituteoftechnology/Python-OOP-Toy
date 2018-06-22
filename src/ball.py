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

class BouncingBall(Ball):
    """
    ball effected by gravity
    """
     
    GRAVITY = .1

    def update(self):
        # This function overrides the update in Ball()
        self.velocity.y += self.GRAVITY
        # Call the parent's update function
        super().update()

class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    GRAVITY = 5
    def update(self):
        self.velocity.y += self.GRAVITY
        r = (self.color[0] + 10) % 256
        g = (self.color[1] -5 ) % 256
        b = (self.color[2] + 5) % 256
        self.color = [r, g, b]
        # Causes all of the balls to bounce
        super().update()
    # TODO: Find out why the balls disappear one by one

class BouncingRainbow(BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    print('This function works!')

class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    
    GRAVITY = .1


    #TODO: They keep sticking and disappearing need to fixed

    def update(self):
        self.velocity.y += self.GRAVITY * self.radius
        super().update()


class KineticBouncing(BouncingBall):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    And is affected by gravity
    """
    
    #TODO:
    pass
    

class AllTheThings(???):
    """
    A ball that does everything!
    """
    #TODO: 
    pass