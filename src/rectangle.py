import math

from pygame.math import Vector2


class Rectangle:
    """
    base class for bouncing objects
    """

    def __init__(self, bounds, position, velocity, color, side):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.side = side

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        # screen width
        if self.position.x < 0 + self.side or self.position.x > self.bounds[0] - self.side:
            self.velocity.x *= -1
        # screen height
        if self.position.y < 0 + self.side or self.position.y > self.bounds[1] - self.side:
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.rect(screen, self.color, [300, 20, 100, 40])


class BouncingRectangle(Rectangle):
    """
    Rectangle effected by gravity
    """
    GRAVITY = .1

    def update(self):
        # This function will override the update in Rectangle()
        self.velocity.y += self.GRAVITY
        # Now that you've done your class specific stuff, call your paren'ts update function
        super().update()


class RainbowRectangle(Rectangle):
    """
    Rectangle that changes colors
    """

    def update(self):
        # TODO: cycle back and forth so color doesn't pop so much
        r = (self.color[0] + 1) % 256
        g = (self.color[1] - 1) % 256
        b = (self.color[2] + 2) % 256
        self.color = [r, g, b]
        super().update()


class BouncingRainbow(BouncingRectangle, RainbowRectangle):
    """
    Rectangle that changes color and is affected by gravity
    """
    pass

# class KineticRectangle(???):
#     """
#     A Rectangle that collides with other collidable Rectangles using simple elastic circle collision
#     """
#     # TODO:

# class KineticBouncing(???):
#     """
#     A Rectangle that collides with other collidable Rectangles using simple elastic circle collision
#     And is affected by gravity
#     """


# class AllTheThings(???):
#     """
#     A Rectangle that does everything!
#     """
