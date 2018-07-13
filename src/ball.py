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
    ball affected by gravity
    """
    
    GRAVITY = 0.3
    
    def update(self):
        # Add gravity then call normal updates
        self.velocity.y += self.GRAVITY
        super().update()        

class RainbowBall(Ball):
    """
    Ball that changes colors
    """

    def update(self):
        r = (self.color[0] + 6) % 256
        g = (self.color[1] + 4) % 256
        b = (self.color[2] - 2) % 256
        self.color = [r, g, b]

        # Call the superclass (Block) update()
        super().update()

class BouncingRainbow(BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    
    pass

# Stretch Goals:

class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    
    def __init__(self, mass, object_list, bounds, position, velocity, color, radius):
        self.object_list = object_list
        super().__init__(bounds, position, velocity, color, radius)
        self.mass = mass

    def collide(self, object, relative_vector):

        tangent = math.atan2(relative_vector.y, relative_vector.x)

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
                    self.collide(object, relative_vector)

        super().update()

class KineticBouncing(BouncingBall, KineticBall):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    And is affected by gravity
    """

    pass
    
class AllTheThings(BouncingBall, KineticBall, RainbowBall):
    """
    A ball that does everything!
    """

    pass