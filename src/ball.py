import math

from pygame.math import Vector2

class Ball:
    """
    base class for bouncing objects
    """
    # Functions just like a JS constructor except...(FINISH) - about 50 min in
    def __init__(self, bounds, position, velocity, color, radius):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.radius = radius
        number = 42
        self.derivedValue = radius * 42

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

        '''
        # html
        <div class = 'coolClass
        '''
# It may be tempting to just copy and paste the above Ball class and alter it, but this is redundant and
# not convention.  Instead, use inheritance!
# Example Exercise: Pass `Ball` in as an argument into `BouncingBall`, and change the `ball` constructor
# in draw.py to `BouncingBall` instead of `Ball`. -- #QUESTION: Ask for more clarity on this!?!?
class BouncingBall(Ball): # Passing Ball in makes BouncingBall a child of Ball
    """ 
    ball effected by gravity
    """
    # TODO: 
    # If you look in Ball class, you will notice that the velocity is defined as `Vector2(3, 3)`
    # # Vector2 is just a class that holds an x and y property for us.  Does common calculations
    # # such as determining distance etc.  See methods here: https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2
    GRAVITY = .1

    # We need to override the update function as it appears in class Ball
    def update(self): #TODO: Fix rounding error that makes ball bounce higher over time
        # print('called update in BouncingBall') # No more bouncingBall
        # upda tes update function y velocity values
        self.velocity.y += self.GRAVITY

        # Now that you've done your class specific stuff, call your parent's update function
        # update function:
        # # This says, once you have made the above changes to self.velocity.y, call the update function above.
        super().update()
    

class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    # TODO: 
    def update(self):
        # Just continuously alters the R, G, and B colors each time update
        # is called.
        r = (self.color[0] + 10) % 256
        g = (self.color[1] - 5) % 256
        b = (self.color[2] + 5) % 256
        self.color = [ r, g, b ]
        # This will get the balls moving!
        super().update()

# class BouncingRainbow(???):
#     """
#     Ball that changes color and is affected by gravity
#     """
#     # TODO:

# class KineticBall(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     """
#     # TODO:

# class KineticBouncing(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """
    

# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """