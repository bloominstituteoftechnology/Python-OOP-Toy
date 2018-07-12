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
    ball affected by gravity
    """
    # TODO:
    def __init__(self, bounds, position, velocity, color, radius, gravity):
        super().__init__(bounds, position, velocity, color, radius)
        self.gravity = gravity #these variable are super finicky

    def update(self):
        friction = .7 # these variables are very finicky
        terminalVelocity = .3

        if self.velocity.y != 0:
            self.velocity.y += self.gravity
        # if velocity is not 0 then you can apply gravity
        # if you apply gravity when velocity is 0, the ball will dip below and be reflected causing a vibrating look

        # adding friction to the x axis
        if self.velocity.x < .1 and self.velocity.x > -.1:
            self.velocity.x = 0
        elif self.velocity.x > 0:
            self.velocity.x -= .005
        else:
            self.velocity.x += .005

        if self.velocity.y > 0 or self.velocity.x != 0: #if ball is moving then do the code, otherwise skip this block
            if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius:
                self.velocity.x *= -1 * friction #reflect x velocity - friction when it bounces off side walls
            if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius:
                if self.velocity.y < terminalVelocity and self.velocity.y > -terminalVelocity:
                    self.velocity.y = 0 
                else:
                    self.velocity.y *= -1 * friction # reflect y velocity - friction when it bounces off floor
        
        self.position += self.velocity



class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    def __init__(self, bounds, position, velocity, color, radius):
        super().__init__(bounds, position, velocity, color, radius)

    def update(self):
        color = random.randint(0,2)
        if color == 0:
            r = (self.color[0] + 10) % 256
            g = self.color[1]
            b = self.color[2]
        elif color == 1:
            r = self.color[0]
            g = (self.color[1] + 10) % 256
            b = self.color[2]
        else:
            r = self.color[0]
            g = self.color[1]
            b = (self.color[2] + 10) % 256
        self.color = [r, g, b]
        super().update()

class BouncingRainbow(BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    def __init__(self, bounds, position, velocity, color, radius, gravity):
        #super().__init__(bounds, position, velocity, color, radius, gravity)
        # super().__init__ passes arguments to first parent
        BouncingBall.__init__(self, bounds, position, velocity, color, radius, gravity)
        # otherwise you can pass arguments to second parent like below but it's not needed here
        #RainbowBall.__init__(self, bounds, position, velocity, color, radius)

    def update(self):
        BouncingBall.update(self)
        RainbowBall.update(self)




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