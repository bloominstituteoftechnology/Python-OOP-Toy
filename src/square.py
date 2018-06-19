import math

from ball import *

from pygame.math import Vector2

class Square:
    """
    base class for bouncing objects
    """
    def __init__(self, bounds, position, velocity, color, width, height):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.width = width
        self.height = height

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        if self.position.x < 0 or self.position.x == self.bounds[0]: # screen width
            self.velocity.x *= 1
        if self.position.y < 100 or self.position.y == self.bounds[1]: # screen height
            self.position.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.rect(screen, self.color, [int(self.position.x), int(self.position.y), int(self.width), int(self.height)],)
    # def rotate(self, screen, pygame):
        pygame.transform.rotate(screen, 5)

class FallingSq(Square):
    """
    ball effected by gravity
    """
   

    GRAVITY = .1

    def update(self):  # TODO: Rounding Error
        # print('called update')
        self.velocity.y += self.GRAVITY 
        super().update()

class RisingSq(Square):

    GRAVITY = .1

    def update(self):
        self.velocity.y -= self.GRAVITY
        super().update()

class BallingSq(Square):
    def debug_create_objects(object_list):
        for i in range(20):
            ball = BouncingBall(SCREEN_SIZE, Vector2(random.randint(100, 400),
                                                    random.randint(100, 400)),
                                                    Vector2(random.random(), random.random()),
                                                    [255, 0, 0], 10)
            object_list.append(ball)

        object_list = [] # list of objects of all types in the toy

        debug_create_objects(object_list)

        for ball in object_list:
            ball.update()
    def update(self):
        super().update()
 

# class RainbowBall(Ball):
#     """
#     Ball that changes colors
#     """
#    # TODO:
#     def update(self):
#         r = (self.color[0] + 10) % 256
#         g = (self.color[1] - 5) % 256
#         b = (self.color[2] + 5) % 256
#         self.color = [r, g, b]
#         super().update()

# class BouncingRainbow(RainbowBall, BouncingBall):
#     """
#     Ball that changes color and is affected by gravity
#     """
#     # TODO:
#     pass

# class KineticBall(BouncingRainbow):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     """
#     # TODO:
#     def update(self):
#         p1 = self.position
#         p2 = self.position
#         v1 = self.velocity
#         v2 = self.velocity
#         b1 = self.bounds
#         b2 = self.bounds

#         if p1.x == p2.x or p1.y == p2.y:
#             v1.x += 5
#             v1.y += 5
#             v2.x += 3
#             v2.y += 3
#             super().update()

# class KineticBouncing(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """
    

# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """