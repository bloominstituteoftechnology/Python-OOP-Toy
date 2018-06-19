import math
import random

from pygame.math import Vector2

class Rectangle:
  """
  base class for rectangles!
  """
  def __init__(self, bounds, color, rect, width):
    self.bounds = bounds
    self.color = color
    self.rect = rect
    self.width = width

  def update(self):
    # TODO: work on movements? eh...maybe
    pass

  def draw(self, screen, pygame):
    # rect(Surface, color, Rect, width=0) --> Rect
    # Draws a rectangular shape on the Surface. The given Rect is the area of the rectangle.
    # The width argument is the thickness to draw the outer edge.
    # If width is zero then the rectangle will be filled.
    # Rect(left, top, width, height) --> Rect
    # Rect((left, top), (width, height)) --> Rect
    # Rect(object) -> Rect
    pygame.draw.rect(screen, self.color, self.rect, self.width)