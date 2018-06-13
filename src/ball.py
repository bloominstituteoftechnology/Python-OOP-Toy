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
        # bounce at edges
        # account for decimal in position # TODO:  Faster to use < and >
        if int(self.position.x) not in range(0 + self.radius, self.bounds[0] - self.radius): # screen width
            self.velocity.x *= -1
        if int(self.position.y) not in range(0 + self.radius, self.bounds[1] - self.radius): # screen height
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)

class BouncingBall(Ball):
    """
    ball effected by gravity
    """
    GRAVITY = .1

    def update(self):
        # add gravity then call normal updates
        self.velocity.y += self.GRAVITY
        super().update()

class RainbowBall(Ball):

    def update(self):
        r = (self.color[0] + 1) % 256
        g = (self.color[1] + 10) % 256
        b = (self.color[2] - 4) % 256
        self.color = [r, g, b]
        super().update()

class BouncingRainbow(BouncingBall, RainbowBall):
    pass

class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    def __init__(self, mass, object_list, bounds, position, velocity, color, radius):
        self.object_list = object_list
        self.mass = mass
        print(position)
        super().__init__(bounds, position, velocity, color, radius)

    def collide(self, object, relative_vector):
        # print('bang!')
        
        # We can imagine the point of reflection as a wall tangent to the collision 
        tangent = math.atan2(relative_vector.y, relative_vector.x)
        # Get the angle of travel for both
        angle1 = 0.5 * math.pi - math.atan2(self.velocity.y, self.velocity.x)
        angle2 = 0.5 * math.pi - math.atan2(object.velocity.y, object.velocity.x)
        # The angles of travel are updated to be two times the tangent minus the current angle
        angle1 = 2 * tangent - angle1
        angle2 = 2 * tangent - angle2

        # Exchange speed
        # Get velocity of other particle
        object_speed = object.velocity.length()
        self_speed = self.velocity.length()

        # Update with new angle and opposing particle's speed
        self.velocity = Vector2(math.sin(angle1), math.cos(angle1)) * object_speed
        object.velocity = Vector2(math.sin(angle2), math.cos(angle2)) * self_speed

        # Fix sticky problem
        # TODO:  This is not efficient or accurate, we should calculate the correct distance and move there exactly
        angle = 0.5 * math.pi + tangent
        while relative_vector.length() <= self.radius + object.radius:
            self.position.x += math.sin(angle)
            self.position.y -= math.cos(angle)
            object.position.x -= math.sin(angle)
            object.position.y += math.cos(angle)
            relative_vector = self.position - object.position

    def update(self):
        # Warning!:  This is a primitive method of collision detection
        # Consider time complexity when adding more of this type
        index = self.object_list.index(self)
        for object in self.object_list[index+1:]:  # TODO: Check effeciency
            if issubclass(type(object), KineticBall) and object != self: # Don't collide with non kinetic (a class is also a subclass of itself)
                # import pdb; pdb.set_trace()
                relative_vector = self.position - object.position
                if relative_vector.length() <= self.radius + object.radius:
                    # We are in collision range, so collide
                    self.collide(object, relative_vector)

        super().update()

class KineticBouncing(BouncingBall, KineticBall):
    pass

class AllTheThings(BouncingBall, KineticBall, RainbowBall):
    pass