from pygame.math import Vector2 as Vector2

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
        # account for decimal in position
        if int(self.position.x) not in range(0 + self.radius, self.bounds[0] - self.radius): # screen width
            self.velocity.x *= -1
        if int(self.position.y) not in range(0 + self.radius, self.bounds[1] - self.radius): # screen height
            self.velocity.y *= -1
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)

class BouncingBall(Ball):
    """
    ball effected by gravity
    """
    GRAVITY = .1

    def update(self):
        # add gravity then call normal update
        self.position.y += self.GRAVITY
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
    def __init__(self, object_list):
        self.object_list = object_list

    def update(self):
        # Warning!:  This is a primitive method of collision detection
        # Consider time complexity when adding more of this type
        for object in self.object_list:
            if object != self and type(object) is KineticBall: # Don't collide with itself or non kinetic
                relativeVector = Vector2(self.position.x - object.x, self.position.y - object.y)
                if relativeVector.length() <= self.radius + object.radius:
                    # We are in collision range, so collide
                    pass


