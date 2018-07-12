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
    # TODO:
    def __init__(self, bounds, position, velocity, color, radius, weight):
      super().__init__(bounds, position, velocity, color, radius)
      self.weight = weight
      self.factorY = 9.8 / weight
      self.gravity = self.factorY
      self.friction = 0.02

    def update(self):
        super().update()
        # print("y", self.position.y)
        self.velocity.y += self.gravity
        self.position.y += self.velocity.y
        if self.position.y + self.radius >= self.bounds[1]:
          self.position.y = self.bounds[1] - self.radius
          if self.gravity >= self.factorY / 1.1:
            print(self.gravity)
            self. gravity += -0.005 * self.factorY / 1.2
            self.velocity.y *= -0.8
            factor = self.velocity.x * 0.2
            self.velocity.x -= factor
          else:
            self.gravity = 0
            self.velocity.y = 0
            self.velocity.x = 0
            self.position.y = self.bounds[1] - self.radius

class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    def __init__(self, bounds, position, velocity, color, radius):
      super().__init__(bounds, position, velocity, color, radius)

    def update(self):
      super().update()

      r = (self.color[0] + 1) % 255
      g = (self.color[1] + 1) % 255
      b = (self.color[2] + 1) % 255

      self.color = (r,g,b)


class BouncingRainbow(BouncingBall,RainbowBall):
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