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
    ball affected by gravity
    """
    # TODO:
    GRAVITY = .03

    def update(self):
        self.velocity.y += self.GRAVITY
        super().update()

class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    # TODO:
    def update(self):
        r = (self.color[0] + 1) % 256
        g = (self.color[1] - 1) % 256
        b = (self.color[2] + 1) % 256
        self.color = [r, g, b]
        super().update()

class BouncingRainbow(BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    # TODO:
    pass
    
class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    # TODO:
    def __init__(self, object_list, bounds, position, velocity, color, radius):
        self.object_list = object_list
        super().__init__(bounds, position, velocity, color, radius)
    
    def update(self):
        super().update()
        for obj in self.object_list:
            if not issubclass(type(obj), KineticBall):
                continue
            if obj == self:
                continue
            
            distance = obj.position.distance_to(self.position)

            sumr = self.radius + obj.radius
            if distance < sumr:
                obj.velocity.reflect_ip(obj.velocity)
                self.velocity.reflect_ip(self.velocity)
                print("There has been a collision!")

class KineticBouncing(KineticBall, BouncingBall):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    And is affected by gravity
    """
    pass
    

# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """