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
    
     def update(self):
            # bounce at edges.  TODO: Fix sticky edges
        self.velocity.y += 0.1
        
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius: # screen width
            self.velocity.x *= -1

        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius: # screen height
            self.velocity.y *= self.weight

            if self.weight < -1.3877787807814457e-16:
                print(self.weight)
                self.weight += 0.1
            
        self.position += self.velocity
        
    # gravity = .2

    # def update(self):
    #     self.velocity.y += self.gravity
    #     super().update()
    
#     """
#     ball effected by gravity
#     """
#     # TODO: 

class RainbowBall(Ball):
    def update(self):
        r = (self.color[0] + 1) % 256
        g = (self.color[1] + 10) % 256
        b = (self.color[2] - 4) % 256
        self.color = [r, g, b]
        super().update()

#     """
#     Ball that changes colors
#     """
#     # TODO:

class BouncingRainbow(RainbowBall, BouncingBall):
    def update(self):
        super().update()
#     """
#     Ball that changes color and is affected by gravity
#     """
#     # TODO:

class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    def __init__(self, mass, object_list, bounds, position, velocity, color, radius):
        self.object_list = object_list
        self.mass = mass
        super().__init__(bounds, position, velocity, color, radius)

    def collide(self, object, relative_vector):
        tangent = math.atan2(relative_vector.y, relative_vector.x)
        # Get the angle of travel for both
        angle1 = 0.5 * math.pi - math.atan2(self.velocity.y, self.velocity.x)
        angle2 = 0.5 * math.pi - math.atan2(object.velocity.y, object.velocity.x)
        angle1 = 2 * tangent - angle1
        angle2 = 2 * tangent - angle2
        object_speed = object.velocity.length()
        self_speed = self.velocity.length()
        self.velocity = Vector2(math.sin(angle1), math.cos(angle1)) * object_speed
        object.velocity = Vector2(math.sin(angle2), math.cos(angle2)) * self_speed
        angle = 0.5 * math.pi + tangent
        while relative_vector.length() <= self.radius + object.radius:
            self.position.x += math.sin(angle)
            self.position.y -= math.cos(angle)
            object.position.x -= math.sin(angle)
            object.position.y += math.cos(angle)
            relative_vector = self.position - object.position

    def update(self):
        index = self.object_list.index(self)
        for object in self.object_list[index+1:]:  
            if issubclass(type(object), KineticBall) and object != self:
                relative_vector = self.position - object.position
                if relative_vector.length() <= self.radius + object.radius:
                    # Objects are in collision range, so collide
                    self.collide(object, relative_vector)

        super().update()

class KineticBouncing(BouncingBall, KineticBall):
    pass

class AllTheThings(BouncingBall, KineticBall, RainbowBall):
    pass
