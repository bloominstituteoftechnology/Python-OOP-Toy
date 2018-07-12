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

# class BouncingBall(???):
#     """
#     ball effected by gravity
#     """
#     # TODO: 

class BouncingBall(Ball):
    """
    ball effected by gravity
    """

    # GRAVITY = .2

    def update(self):
        #self.velocity.y += self.GRAVITY
        self.velocity.y += .2
        super().update()


# class RainbowBall(???):
#     """
#     Ball that changes colors
#     """
#     # TODO:

class RainbowBall(Ball):
    """
    Ball that changes colors
    """

    def update(self):
        r = (self.color[0] + 10) % 256
        g = (self.color[1] - 5) % 256
        b = (self.color[2] + 5) % 256

        self.color = [r, g, b]

        #call the superclass (Block) update()
        super().update()

# class BouncingRainbow(???):
#     """
#     Ball that changes color and is affected by gravity
#     """
#     # TODO:


class BouncingRainbow(BouncingBall, RainbowBall):
    pass


# class KineticBall(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     """
#     # TODO:

class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    def __init__(self, object_list, bounds, position, velocity, color, radius):
        self.object_list = object_list
        super().__init__(bounds, position, velocity, color, radius)

    def update(self):
        for obj in self.object_list:

            if not issubclass(type(obj), KineticBall):
                continue

            if obj == self:
                continue

            distance = obj.position.distance_to(self.position)

            sum_radius = self.radius + obj.radius

            if distance < sum_radius:
                print('Ping Ping!')


# class KineticBouncing(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """

class KineticBouncing(BouncingBall, KineticBall):
    """
     A ball that collides with other collidable balls using simple elastic circle collision
    And is affected by gravity
    """
    pass

# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """

class AllTheThings(BouncingBall, KineticBall, RainbowBall):
    """
    A ball that does everything!
    """
    pass