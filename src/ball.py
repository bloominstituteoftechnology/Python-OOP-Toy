import math

from pygame.math import Vector2


class Ball:
    """
    base class for bouncing objects
    """
    FRICTION = .2

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
            self.velocity.x -= self.FRICTION
            self.velocity.x *= -1

        # screen height
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius:
            self.velocity.x += (self.FRICTION / 2) if self.velocity.x < 0 else - \
                (self.FRICTION / 2)
            self.velocity.y -= self.FRICTION
            self.velocity.y *= -1

        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(
            self.position.x), int(self.position.y)], self.radius)


class BouncingBall(Ball):
    """
    ball effected by gravity
    """
    # TODO:
    GRAVITY = .1

    def update(self):  # TODO: Fix rounding error that makes it bounce higher.
        self.velocity.y += self.GRAVITY
        print(self.velocity.y)
        # Now that your done, call parent's update function
        super().update()


class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    # TODO:

    def update(self):
        self.color[0] = (self.color[0] - 10) % 256
        self.color[1] = (self.color[1] - 5) % 256
        self.color[2] = (self.color[2] + 5) % 256

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
    # TODO:
    self.rect.col

# class KineticBouncing(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """


# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """
