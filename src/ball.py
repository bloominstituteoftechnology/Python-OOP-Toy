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
        # screen width
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius:
            self.velocity.x *= -1
        # screen height
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius:
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(
            self.position.x), int(self.position.y)], self.radius)


class BouncingBall(Ball):
    """
    ball affected by gravity
    """
    GRAVITY = .1

    def update(self):
        self.velocity.y += self.GRAVITY
        # print('called update(self) in BouncingBall')
        super().update()


class RainbowBall(Ball):
    """
    Ball that changes colors
    """

    def update(self):
        r = (self.color[0] + 1) % 256
        g = (self.color[1] - 1) % 256
        b = (self.color[2] + 1) % 256
        self.color = [r, g, b]
        super().update()

        # r = (self.color[0] + 10)
        # g = (self.color[1] - 5)
        # b = (self.color[2] + 5)
        # for r in range(256):
        #     for g in range(256):
        #         for b in range(256):
        #             self.color = [r, g, b]

        # color_provider = update(self)
        # for x in range(1000):
        #     for y in range(1000):
        #         set_pixel(x, y, color=next(color_provider))
        # super().update()


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
