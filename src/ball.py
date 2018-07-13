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
        if self.position.x < 5 + self.radius or self.position.x > self.bounds[0] - self.radius: # screen width
            self.velocity.x *= -1
        if self.position.y < 5 + self.radius or self.position.y > self.bounds[1] - self.radius: # screen height
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)

class BouncingBall(Ball):
#     """
#     ball effected by gravityadsfasdf
#     """
    
    def __init__(self, weight, bounds, position, velocity, color, radius):
        super().__init__(bounds, position, velocity, color, radius)
        self.weight = weight
    
    def update(self):
        if self.position.x > 0 + self.radius or self.position.x > self.bounds[0] - self.radius:
            self.velocity.y += 0.1
            super().update()
#     # TODO: 

class RainbowBall(Ball):
    def update(self):
        r = (self.color[0] + 3) % 256
        g = (self.color[1] + 2) % 256
        b = (self.color[2] - 1) % 256
#
        self.color = [r, g, b]
        super().update()
#     """
#     Ball that changes colors
#     """
#     # TODO:

class BouncingRainbow(RainbowBall, BouncingBall):
    
    pass
    
#     """
#     Ball that changes color and is affected by gravity
#     """
#     # TODO:

class KineticBall(Ball):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     """
    # #     # TODO:
    
    def __init__(self, object_list, bounds, position, velocity, color, radius):
        self.object_list = object_list
        super().__init__(bounds, position, velocity, color, radius)
    
    def update(self):
        for object in self.object_list:
            if object == self:
                continue

            distance = object.position.distance_to(self.position)
            sumr = self.radius + object.radius

            if distance < sumr:
                print('collision!')
        super().update()

class KineticBouncing(KineticBall, BouncingBall):
    
    def __init__(self, object_list, bounds, position, velocity, color, radius, weight):
        super().__init__(object_list, bounds, position, velocity, color, radius, weight)
        
        BouncingBall.update(self)    
        KineticBall.update(self)
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """
    

# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """
