import math

from pygame.math import Vector2

class Rect:
    """
    base class for bouncing objects
    """
    # Functions just like a JS constructor except...(FINISH) - about 50 min in
    def __init__(self, bounds, position, velocity, color, width, height):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.width = width
        self.height = height
        # number = 42
        # self.derivedValue = radius * 42

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        if self.position.x < 0 or self.position.x > self.bounds[0] - self.width:# screen width
            self.velocity.x *= -1
        if self.position.y < 0 or self.position.y > self.bounds[1] - self.height: # screen height
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.rect(screen, self.color, ( self.position.x, self.position.y, self.width, self.height))

        '''
        # html
        <div class = 'coolClass
        '''
# It may be tempting to just copy and paste the above Rect class and alter it, but this is redundant and
# not convention.  Instead, use inheritance!
# Example Exercise: Pass `Rect` in as an argument into `BouncingRect`, and change the `Rect` constructor
# in draw.py to `BouncingRect` instead of `Rect`. -- #QUESTION: Ask for more clarity on this!?!?
class BouncingRect(Rect): # Passing Rect in makes BouncingRect a child of Rect
    """ 
    Rect effected by gravity
    """
    # TODO: 
    # If you look in Rect class, you will notice that the velocity is defined as `Vector2(3, 3)`
    # # Vector2 is just a class that holds an x and y property for us.  Does common calculations
    # # such as determining distance etc.  See methods here: https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2
    GRAVITY = .1

    # We need to override the update function as it appears in class Rect
    def update(self): #TODO: Fix rounding error that makes Rect bounce higher over time
        # print('called update in BouncingRect') # No more bouncingRect
        # upda tes update function y velocity values
        self.velocity.y += self.GRAVITY

        # Now that you've done your class specific stuff, call your parent's update function
        # update function:
        # # This says, once you have made the above changes to self.velocity.y, call the update function above.
        super().update()
    

class RainbowRect(Rect):
    """
    Rect that changes colors
    """
    # TODO: 
    def update(self):
        # Just continuously alters the R, G, and B colors each time update
        # is called.
        r = (self.color[0] + 2) % 256
        g = (self.color[1] - 1) % 256
        b = (self.color[2] + 0.5) % 256
        self.color = [ r, g, b ]
        # This will get the Rects moving!
        super().update()

class BouncingRainbow(BouncingRect, RainbowRect): # That's it!  Everything you need is already in the previously constructed instances!
    """
    Rect that changes color and is affected by gravity
    """

# class BouncingRectangles(BouncingRect):
#     """
#     A Rect that collides with other collidable Rects using simple elastic circle collision
#     """
#     # TODO:
#     def draw(self):
#         pygame.draw.rect(screen, self.color, 100, width=10)
#         super().draw()


class KineticRect(BouncingRect):
    """
    A Rect that collides with other collidable Rects using simple elastic circle collision
    """
    # TODO:

# class KineticBouncing(???):
#     """
#     A Rect that collides with other collidable Rects using simple elastic circle collision
#     And is affected by gravity
#     """
    

# class AllTheThings(???):
#     """
#     A Rect that does everything!
#     """