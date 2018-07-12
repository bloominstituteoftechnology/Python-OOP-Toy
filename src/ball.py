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
        self.maxHeight = self.radius + 2
        self.reduce = self.bounds[1]/3

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius/2: # screen width
            self.velocity.x *= -1
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius/2: # screen height
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)

class BouncingBall(Ball):
    """
    ball effected by gravity
    """
    def update(self):
        # super().update()
        print(self.velocity.y, self.position.y, self.bounds[1] - self.radius)
        self.velocity.x = 0

        if (self.velocity.y > 0-self.radius/2 and self.velocity.y < self.radius/2 and self.position.y >= self.bounds[1] - self.radius):
            self.velocity.y = 0
        else:
            self.velocity.y += 0.2      
            
        if self.position.y > self.bounds[1]: # screen height
            self.velocity.y -= 0.8
            self.velocity.y *= -1
            
        
        # if self.velocity.y < 0:
            

        self.position += self.velocity
        # if self.maxHeight >= (self.bounds[1] - 0.001):
        #     self.velocity.y = 0
        # else:
        #     if (self.velocity.y < 0 and self.position.y < self.maxHeight) or self.position.y >= self.bounds[1] - self.radius:                
        #         self.velocity.y *= -0.7
        #         self.reduce = self.maxHeight
        #         self.maxHeight += (self.bounds[1] - self.reduce)/3
        #     if self.velocity.y > 0:
        #         self.velocity.y += 0.01

        # self.position += self.velocity


class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    def update(self):
        r = (self.color[0]+3) % 256
        g = (self.color[1]+2) % 256
        b = (self.color[2]-1) % 256

        self.color = [r,g,b]

        super().update()

class BouncingRainbow(RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    def update(self):
        self.velocity.x = 0
        super().update()

class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    def __init__(self, objects_list, bounds, position, velocity, color, radius):
        self.objects_list = objects_list
        super().__init__(bounds, position, velocity, color, radius)

    def update(self):
        super().update()
        for obj in self.objects_list:
            if not issubclass(type(obj), KineticBall):
                continue

            if obj ==  self:
                continue
            
            distance = obj.position.distance_to(self.position)

            sumr = self.radius + obj.radius

            if distance < sumr:
                print("Collision!")
                obj.velocity.x *= -1
                obj.velocity.y *= -1


# class KineticBouncing(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """
    

# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """