import math
import time


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
            print(time.time(), time.clock())
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)

class BouncingBall(Ball):
    def __init__(self,bounds, position, velocity, color, radius):
        super().__init__(bounds, position, velocity, color, radius)
    """
    ball effected by gravity
    """

    # # TODO: 
    def update(self):
        self.velocity.y += 0.07
        super().update()
      


class RainbowBall(Ball):
    def __init__(self,bounds, position, velocity, color, radius):
        super().__init__(bounds, position, velocity, color, radius)
    """
    Ball that changes colors
    """
    # TODO:
    def update(self):
        r = (self.color[0] + 3) % 256
        g = (self.color[1] + 2) % 256
        b = (self.color[2] - 1) % 256

        self.color = [r, g, b]
        super().update()

class BouncingRainbow(RainbowBall, BouncingBall):
    """
    Ball that changes color and is affected by gravity
    """
    pass


class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    # TODO:
    def __init__(self,object_list,bounds,position,velocity,color,radius) #overrides constructor with a new one
        self.object_list = object_list #pass object list into classes properties
        super().__init__(bounds,position,velocity,color,radius) # inherit from previous classes
    def update(self):
        for obj in object_list:
            x0 = self.position.x #represents where ball is on x axis
            y0 = self.position.y #represents where ball is on y axis

            for obj in self.object_list:
                distance = obj.position.distance_to(self_position)

                sumr = self.radius + obj.radius

                if distance < sumr:
                    print("Collision detected")

# class KineticBouncing(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """
    

# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """