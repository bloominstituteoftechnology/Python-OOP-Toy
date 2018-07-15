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
        if (
            self.position.x < 0 + self.radius
            or self.position.x > self.bounds[0] - self.radius
        ):  # screen width
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius: # screen width
        if (
            self.position.y < 0 + self.radius
            or self.position.y > self.bounds[1] - self.radius
        ):  # screen height
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius: # screen height
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        pygame.draw.circle(
            screen,
            self.color,
            [int(self.position.x), int(self.position.y)],
            self.radius,
        )

        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)

# class BouncingBall(???):
#     """
#     ball effected by gravity
#     # TODO:
#     # TODO: 

# class RainbowBall(???):
#     """
#     Ball that changes colors
#     """
#     # TODO:

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

    

# class AllTheThings(???):
#     """
#     A ball that does everything!

