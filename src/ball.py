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
    def __init__(self, bounds, position, velocity, color, radius, weight):
        super().__init__(bounds, position, velocity, color, radius)
        self.weight = weight

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        self.velocity.y += 0.1
        
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius: # screen width
            self.velocity.x *= -1

        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius: # screen height
            self.velocity.y *= self.weight

            if self.weight < -1.3877787807814457e-16:
                self.weight += 0.1
            
        self.position += self.velocity

    # TODO: 

class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    # TODO:
    def __init__(self, bounds, position, velocity, color, radius):
        super().__init__(bounds, position, velocity, color, radius)

    def change_colors(self):
        self.color[0] += 1
        self.color[1] += 5
        self.color[2] += 20

        if self.color[0] >= 255:
            self.color[0] = 0

        if self.color[1] >= 255:
            self.color[1] = 0

        if self.color[2] >= 255:
            self.color[2] = 0

class BouncingRainbow(BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    # TODO:
    def __init__(self, bounds, position, velocity, color, radius, weight):
        super().__init__(bounds, position, velocity, color, radius, weight)

class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    def __init__(self, bounds, position, velocity, color, radius, object_list):
        super().__init__(bounds, position, velocity, color, radius)
        self.object_list = object_list
    
    def update(self):
        super().update()

        for obj in self.object_list:
            if not issubclass(type(obj), KineticBall):
                continue

            if obj == self:
                continue

            distance = obj.position.distance_to(self.position)
            sumr = self.radius + obj.radius

            if distance < sumr:
                self.velocity.x *= -1; self.velocity.y *= -1

class KineticBouncing(BouncingBall):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    And is affected by gravity
    """
    def __init__(self, bounds, position, velocity, color, radius, weight, object_list):
        super().__init__(bounds, position, velocity, color, radius, weight)
        self.object_list = object_list

    def update(self):
        super().update()

        for obj in self.object_list:
            if not issubclass(type(obj), KineticBouncing):
                continue

            if obj == self:
                continue

            distance = obj.position.distance_to(self.position)
            sumr = self.radius + obj.radius

            if distance < sumr:
                self.velocity.x *= -1; self.velocity.y *= -1

class AllTheThings(KineticBouncing):
    """
    A ball that does everything!
    """
    # def __init__(self, bounds, position, velocity, color, radius, weight, object_list):
    #     super()__init__(bounds, position, velocity, color, radius, weight, object_list)

    def update(self):
        super().update()

        self.color[0] += 1
        self.color[1] += 5
        self.color[2] += 20

        if self.color[0] >= 255:
            self.color[0] = 0

        if self.color[1] >= 255:
            self.color[1] = 0

        if self.color[2] >= 255:
            self.color[2] = 0