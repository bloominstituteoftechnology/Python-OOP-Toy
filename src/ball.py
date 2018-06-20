import math
import random

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
        # bounce at edges.  TODO: I think sticky edges are fixed...
        # if self.position.x <= 0 + self.radius or self.position.x >= self.bounds[0] - self.radius: # screen width
        if (self.position.x + self.radius) >= self.bounds[0]: # screen width
            self.velocity.x *= -1
            self.position.x = self.bounds[0] - self.radius
        if (self.position.x - self.radius) <= 0:
            self.velocity.x *= -1
            self.position.x = self.radius
        # if self.position.y <= 0 + self.radius or self.position.y >= self.bounds[1] - self.radius: # screen height
        if (self.position.y + self.radius) >= self.bounds[1]:
            self.velocity.y *= -1
            self.position.y = self.bounds[1] - self.radius
        if (self.position.y - self.radius) <= 0: # screen height
            self.velocity.y *= -1
            self.position.y = self.radius

        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)

class BouncingBall(Ball):
    """
    ball effected by gravity
    """
    GRAVITY = 0.15

    def update(self):
        # This fn overrides update() in Ball
        self.velocity.y += self.GRAVITY
        # Now that you've done your class specific stuff, call your parent's update() fn
        super().update()

class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    
    def update(self):
        # self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255) ]
        r = (self.color[0] + 5) % 256
        g = (self.color[1] - 1) % 256
        b = (self.color[2] + 2) % 256
        self.color = [r, g, b]
        super().update()

class BouncingRainbow(BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    # Just have to inherit from BouncingBall and RainbowBall == Done!
    pass

class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    def __init__(self, bounds, position, velocity, color, radius, mass, object_list):
        self.object_list = object_list
        self.mass = mass
        super().__init__(bounds, position, velocity, color, radius)

    # Reference source: https://blogs.msdn.microsoft.com/faber/2013/01/09/elastic-collisions-of-balls/
    def _collide(self, obj, rel_vector):
        collision_angle = math.atan2(rel_vector.y, rel_vector.x)
        speed1 = self.velocity.length()
        speed2 = obj.velocity.length()
        dir1 = math.atan2(self.velocity.y, self.velocity.x)
        dir2 = math.atan2(obj.velocity.y, obj.velocity.x)

        new_xspeed_1 = speed1 * math.cos(dir1 - collision_angle)
        new_yspeed_1 = speed1 * math.sin(dir1 - collision_angle)
        new_xspeed_2 = speed2 * math.cos(dir2 - collision_angle)
        new_yspeed_2 = speed2 * math.sin(dir2 - collision_angle)

        final_xspeed_1 = ((self.mass - obj.mass) * new_xspeed_1 + (2 * obj.mass) * new_xspeed_2) / (self.mass + obj.mass)
        final_xspeed_2 = ((self.mass + self.mass) * new_xspeed_1 + (obj.mass - self.mass) * new_xspeed_2) / (self.mass + obj.mass)
        final_yspeed_1 = new_yspeed_1
        final_yspeed_2 = new_yspeed_2

        cos_coll_angle = math.cos(collision_angle)
        sin_coll_angle = math.sin(collision_angle)

        self.velocity.x = cos_coll_angle * final_xspeed_1 - sin_coll_angle * final_yspeed_1
        self.velocity.y = sin_coll_angle * final_xspeed_1 + cos_coll_angle * final_yspeed_1
        obj.velocity.x = cos_coll_angle * final_xspeed_2 - sin_coll_angle * final_yspeed_2
        obj.velocity.y = sin_coll_angle * final_xspeed_2 + cos_coll_angle * final_yspeed_2

        pos1 = self.position
        pos2 = obj.position

        posDiff = pos1 - pos2
        d = math.sqrt(posDiff.x * posDiff.x + posDiff.y * posDiff.y)

        # minimum translation distance (mtd)
        mtd = posDiff * (((self.radius + obj.radius) - d) / d)
        # resolve intersection -- computing inverse mass quantitites
        im1 = 1 / self.mass
        im2 = 1 / obj.mass

        # push-pull them apart based off their masses
        pos1 = pos1 + mtd * (im1 / (im1 + im2))
        pos2 = pos2 - mtd * (im2 / (im1 + im2))

        self.position = pos1
        obj.position = pos2

    def update(self):
        idx = self.object_list.index(self)
        for obj in self.object_list[idx + 1:]:
            if issubclass(type(obj), KineticBall) and obj != self:
                rel_vector = self.position - obj.position
                if rel_vector.length() <= self.radius + obj.radius:
                    self._collide(obj, rel_vector)

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