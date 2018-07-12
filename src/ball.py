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
    # TODO: create another bouncing ball
    def update(self): 
        
        self.velocity.x *= +1
        self.velocity.y *= +1

        super().update()

class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    # TODO: create a rainbow ball

    def update(self):
        r = (self.color[0] + 3) % 256
        g = (self.color[1] + 2) % 256
        b = (self.color[2] - 1) % 256
        
        self.color = [r, g, b]

        super().update()

class BouncingRainbow(BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    pass
    
# class BouncingRainbow(Ball):
#     """
#     Ball that changes color and is affected by gravity
#     """
#     # TODO: create a bouncing rainbow ball 

#     def update(self):
#         r = (self.color[0] + 3) % 256
#         g = (self.color[1] + 2) % 256
#         b = (self.color[2] + 1) % 256

#         self.color = [r, g, b]        

#         super().update()

# Stretch Goals 

class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    def __init__(self, object_list, bounds, position, velocity, color, radius):
        self.object_list = object_list
        super().__init__(bounds, position, velocity, color, radius)

    
    def update(self):
        for obj in self.object_list:

            if not issubclass(type(obj), KineticBall):
                continue

            if obj == self:
                continue 

            distance = obj.position.distance_to(self.position)

            sumr = self.radius + obj.radius

            if distance < sumr: 
                print("Collision!")


    # def update(self):
    #     x0 = self.position.x
    #     y0 = self.position.y

    #     for obj in self.object_lists:
    #         x1 = obj.position.x
    #         y1 = obj.position.y 

    #         diffx = x1 = x0 
    #         diffy = y1 - y0 

    #         distance = math.sqrt(diffx**2 + diffy**2)

    #         sumr = self.radius + obj.radius

    #         if distance < sumr:
    #             print("Collision!")
            

# class KineticBouncing(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """
    

# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """