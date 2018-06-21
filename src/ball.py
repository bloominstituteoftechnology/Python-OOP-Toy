import math

from pygame.math import Vector2
from pygame import Rect

from block import KineticBlock

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
        self.collision_rectangle = self.update_rectangle()

    def update_rectangle(self):
        return Rect(self.position.x - self.radius,
                                        self.position.y - self.radius,
                                        self.radius*2, self.radius*2)

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        if self.position.x <= 0 + self.radius: # screen width
            self.position.x = self.radius + 1
            self.velocity.x *= -1
        if self.position.x >= self.bounds[0] - self.radius:
            self.position.x = self.bounds[0] - self.radius - 1
            self.velocity.x *= -1
        if self.position.y <= 0 + self.radius: # screen height
            self.position.y = self.radius + 1
            self.velocity.y *= -1
        if self.position.y >= self.bounds[1] - self.radius:
            self.position.y = self.bounds[1] - self.radius - 1
            self.velocity.y *= -1

        self.position += self.velocity
        self.collision_rectangle = self.update_rectangle()

    def check_collision(self):
        # No collision on base models
        pass

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
    and collides with collidable rectangles as well
    """
    def __init__(self, mass, object_list, bounds, position, velocity, color, radius):
        self.object_list = object_list
        self.mass = mass
        super().__init__(bounds, position, velocity, color, radius)

    def collide_with_ball(self, object, relative_vector):
        print('bang!')

        while relative_vector.length() <= self.radius + object.radius:
            self.position += relative_vector.normalize()
            object.position -= relative_vector.normalize()
            relative_vector = self.position - object.position

        # Help sticky problem
        # TODO:  This is not efficient or accurate, we should calculate the correct distance and move there exactly
        # angle = 0.5 * math.pi + tangent
        # test = Vector2(math.cos(angle), math.sin(angle))
        # print(test)
        # while relative_vector.length() <= self.radius + object.radius:
        #     object.position -= relative_vector.normalize()
        #     self.position += relative_vector.normalize()
        # #     self.position.x += math.sin(angle)
        # #     self.position.y -= math.cos(angle)
        # #     object.position.x -= math.sin(angle)
        # #     object.position.y += math.cos(angle)
        #     relative_vector = self.position - object.position
        
        # We can imagine the point of reflection as a wall tangent to the collision 
        tangent = math.atan2(relative_vector.y, relative_vector.x)

        plane = relative_vector
        self_speed = self.velocity.length()
        object_speed = object.velocity.length()
        self.velocity = self.velocity.reflect(plane).normalize()
        self.velocity *= object_speed
        object.velocity = object.velocity.reflect(plane).normalize()
        object.velocity *= self_speed

        
        # # Get the angle of travel for both
        # angle1 = 0.5 * math.pi - math.atan2(self.velocity.y, self.velocity.x)
        # angle2 = 0.5 * math.pi - math.atan2(object.velocity.y, object.velocity.x)
        # # The angles of travel are updated to be two times the tangent minus the current angle
        # angle1 = 2 * tangent - angle1
        # angle2 = 2 * tangent - angle2

        # # Exchange speed
        # # Get velocity of other particle
        # object_speed = object.velocity.length()
        # self_speed = self.velocity.length()

        # print('before', self.velocity.length())
        # # Update with new angle and opposing particle's speed
        # # self.velocity = Vector2(math.cos(angle2), math.sin(angle2)).normalize() * object_speed
        # # object.velocity = Vector2(math.cos(angle1), math.sin(angle1)).normalize() * self_speed

        # # original
        # self.velocity = Vector2(math.cos(angle1), math.sin(angle1)) * object_speed
        # object.velocity = Vector2(math.cos(angle2), math.sin(angle2)) * self_speed
        # print('after', self.velocity.length())

    def collide_with_rectangle(self, object):
        # This function is called after a first-pass test, that is the collision
        # rectangles overlap. 
        # First, check that collision actually happened
        # Then, bounce appropriately
        left, right, top, bottom = False, False, False, False
        # TODO:  This can probably be optimized
        if (
            object.position.x > self.position.x and
            object.position.x - object.rectangle.width/2 <= self.position.x + self.radius and 
            self.position.y <= object.position.y+object.rectangle.height/2 and 
            self.position.y >= object.position.y - object.rectangle.height/2
        ):
            left = True

        if (
            object.position.x < self.position.x and
            object.position.x + object.rectangle.width/2 >= self.position.x - self.radius and 
            self.position.y <= object.position.y+object.rectangle.height/2 and 
            self.position.y >= object.position.y - object.rectangle.height/2
        ):
            right = True

        if (
            object.position.y > self.position.y and
            object.position.y - object.rectangle.height/2 <= self.position.y + self.radius and 
            self.position.x <= object.position.x+object.rectangle.width/2 and 
            self.position.x >= object.position.x - object.rectangle.width/2
        ):
            top = True

        if (
            object.position.y < self.position.y and
            object.position.y + object.rectangle.width/2 >= self.position.y - self.radius and 
            self.position.x <= object.position.x+object.rectangle.width/2 and 
            self.position.x >= object.position.x - object.rectangle.width/2
        ):
            bottom = True

        test = left + right + top + bottom
        
        if test == 1:
            # the ball has collided with an edge
            if left or right:
                self.velocity.x *= -1
                # fix sticky edges
                if left:
                    self.position.x = object.position.x - object.rectangle.width/2 - self.radius - 1
                else:
                    self.position.x = object.position.x + object.rectangle.width/2 + self.radius + 1

            if top or bottom:
                self.velocity.y *= -1
                if top:
                    self.position.y = object.position.y - object.rectangle.height/2 - self.radius - 1
                else:
                    self.position.y = object.position.y + object.rectangle.height/2 + self.radius + 1

        elif test == 4:
            # TODO:  Better error handling
            print('error:  ball inside rectangle')

        elif test == 0:
            # We are at a corner.  Either it narrowly missed, or it hit the corner
            corners = [
                Vector2(object.position.x - object.rectangle.width/2, object.position.y - object.rectangle.height/2),
                Vector2(object.position.x + object.rectangle.width/2, object.position.y - object.rectangle.height/2),
                Vector2(object.position.x - object.rectangle.width/2, object.position.y + object.rectangle.height/2),
                Vector2(object.position.x + object.rectangle.width/2, object.position.y + object.rectangle.height/2)
            ]

            for corner in corners:
                relative_vector = self.position - corner
                if relative_vector.length() <= self.radius:
                    print('corner')
                    # Create a dummy object to make use of ball to ball collision, because the math is the same
                    # Give it a velocity of the same magnitude as the current ball to cause it to reflect
                    stand_in = Ball(self.bounds, corner, Vector2(0, self.velocity.length()), [0,0,0], 0)
                    self.collide_with_ball(stand_in, relative_vector)



    def update(self):
        # Warning!:  This is a primitive method of collision detection
        # Consider time complexity when adding more of this type
        index = self.object_list.index(self)
        for object in self.object_list[index+1:]:  # TODO: Check effeciency
            # Don't collide with non kinetic (a class is also a subclass of itself)
            # Balls colliding with balls
            if issubclass(type(object), KineticBall) and object != self:
                relative_vector = self.position - object.position
                if relative_vector.length() <= self.radius + object.radius:
                    # Objects are in collision range, so collide
                    self.collide_with_ball(object, relative_vector)
            # Balls colliding with rectangles
            elif issubclass(type(object), KineticBlock) and object != self:
                # Do a first round pass for collision (we know object is a KineticBlock)
                if self.collision_rectangle.colliderect(object.rectangle):
                    self.collide_with_rectangle(object)

        super().update()

class KineticBouncing(BouncingBall, KineticBall):
    pass

class AllTheThings(BouncingBall, KineticBall, RainbowBall):
    pass