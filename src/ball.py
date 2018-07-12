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

    # Original code:
    # def update(self):
    #     # bounce at edges.  TODO: Fix sticky edges
    #     if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius: # screen width
    #         self.velocity.x *= -1
    #     if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius: # screen height
    #         self.velocity.y *= -1
    #     self.position += self.velocity

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        if self.position.x < 0 + self.radius:
            self.position.x = 0 + self.radius
            self.velocity.x *= -1
        elif self.position.x > self.bounds[0] - self.radius:
            self.position.x = self.bounds[0] - self.radius
            self.velocity.x *= -1
        if self.position.y < 0 + self.radius:
            self.position.y = 0 + self.radius
            self.velocity.y *= -1
        elif self.position.y > self.bounds[1] - self.radius:
            self.position.y = self.bounds[1] - self.radius
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)

class BouncingBall(Ball):
    """
    ball affected by gravity
    """
    # Check Lecture 14-4 at 50 minutes
    GRAVITY = 0.1

    def update(self):
        self.velocity.y += self.GRAVITY
        super().update()
        

class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    def update(self):
        # credit:
        # https://stackoverflow.com/questions/30099435/vpython-gradually-change-colors
        r = self.color[0] 
        g = self.color[1]
        b = self.color[2]
        increment = 10
        if r == 255 and g != 255 and b == 0:
            g += increment
            if g > 255: g = 255
        elif r != 0 and g == 255 and b == 0:
            r -= increment
            if r < 0: r = 0
        elif r == 0 and g == 255 and b != 255:
            b += increment
            if b > 255: b = 255
        elif r == 0 and g != 0 and b == 255:
            g -= increment
            if g < 0: g = 0
        elif r != 255 and g == 0 and b == 255:
            r += increment
            if r > 255: r = 255
        elif r == 255 and g == 0 and b != 0:
            b -= increment
            if b < 0: b = 0
        self.color = [r, g, b]
        super().update()
    

class BouncingRainbow(BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    pass

class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    def __init__(self, bounds, position, velocity, color, radius):
        super().__init__(bounds, position, velocity, color, radius)
        self.old_position = position
        self.entities = []
        self.collidable = True
    
    def update(self):
        self.old_position = self.position
        super().update()

        # credit:
        # https://www.youtube.com/watch?v=0OiQk2CiBAY
        for a in self.entities:

            if a == self: continue
            
            d = a.position.distance_to(self.position)

            if d < (a.radius + self.radius):
                overlap = a.radius + self.radius - d
            
                dir = self.position - a.position
                dir.scale_to_length(overlap / 2)

                a.position -= dir
                self.position += dir
            
                a.velocity.reflect_ip(a.velocity)
                self.velocity.reflect_ip(self.velocity)


class KineticBouncing(BouncingBall, KineticBall):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    And is affected by gravity
    """
    pass

class AllTheThings(KineticBall, BouncingBall, RainbowBall):
    """
    A ball that does everything!
    """
    pass