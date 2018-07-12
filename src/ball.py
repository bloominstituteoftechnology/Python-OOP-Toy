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


    """ def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius: # screen width
            self.velocity.x *= -1
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius: # screen height
            self.velocity.y *= -1
        self.position += self.velocity"""

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
    GRAVITY = 0.1

    # TODO: 
    def update(self):
        self.velocity.y += self.GRAVITY
        super().update()
        

class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    # TODO:
    def update(self):
        r = (self.color[0] + 2) % 256 
        g = (self.color[1] + 4) % 256
        b = (self.color[2] + 6) % 256

        self.color = [r, g, b]
        super().update()

class BouncingRainbow(BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    # TODO:
    pass


# class KineticBall(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     """
#     # TODO:
class KineticBall(Ball):
    def __init__(self, bounds, position, velocity, color, radius):
        self.object_list = []
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

class KineticBouncing(KineticBall, BouncingBall):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """
    pass
    

class AllTheThings(BouncingRainbow, KineticBall):
#     """
#     A ball that does everything!
#     """
    pass