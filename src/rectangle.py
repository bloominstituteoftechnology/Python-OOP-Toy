import math

from pygame.math import Vector2

class Rectangle:
  # Base class for bouncing rectangles
  def __init__(self, bounds, position, velocity, color, length):
    self.bounds = bounds
    self.position = position
    self.velocity = velocity
    self.color = color
    self.length = length

  def update(self):
    # bounce at edges.  FIXED: Fix sticky edges
    if self.position.x < 0 + self.length or self.position.x > self.bounds[0] - self.length: # screen width
      self.velocity.x *= -1
    if self.position.y < 0 + (self.length + 1) or self.position.y > self.bounds[1] - self.length: # screen height
      if self.position.y < 0 + self.length:
        self.position.y += 1
      self.velocity.y *= -1
    self.position += self.velocity

  def draw(self, screen, pygame):
      # cast x and y to int for drawing
      pygame.draw.rect(screen, self.color, [int(self.position.x), int(self.position.y), self.length, self.length], 50)
