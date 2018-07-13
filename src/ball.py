import math

from pygame.math import Vector2

class Ball:
    """
    base class for bouncing objects - base class is the root class that other classes inherit from
    """
    def __init__(self, bounds, position, velocity, color, radius):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.radius = radius

    def update(self): #this is a method
        # bounce at edges.  TODO: Fix sticky edges
        nxt = self.position + self.velocity
        left_edge_nxt = nxt.x < 0 + self.radius
        right_edge_nxt = nxt.x > self.bounds[0] - self.radius
        top_edge_nxt = nxt.y < 0 + self.radius
        bottom_edge_nxt = nxt.y > self.bounds[1] - self.radius
        
        if left_edge_nxt:
            self.position.x = self.radius * 2 - nxt.x
            self.velocity.x *= -1
        elif right_edge_nxt:
            self.position.x = (self.bounds[0] - self.radius) * 2 - nxt.x
            self.velocity.x *= -1
        else: 
            self.position.x += self.velocity.x

        if top_edge_nxt:
            self.position.y = self.radius * 2 - nxt.y
            self.velocity.y *= -1
        elif bottom_edge_nxt:
            self.position.y = (self.bounds[1] - self.radius) * 2 - nxt.y
            self.velocity.y *= -1
        else:
            self.position.y += self.velocity.y

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)

class BouncingBall(Ball):
    def __init__(self, bounds, position, velocity, color, radius, gravity):
        self.gravity = gravity
        super().__init__(bounds, position, velocity, color, radius)
#     """
#     ball affected by gravity
#     """
#     # TODO: update

    def update(self):
        self.velocity.y += self.gravity
        super().update()    


class RainbowBall(Ball):
#     """
#     Ball that changes colors
#     """
#     # TODO: update

    def update(self):
        r = (self.color[0]+ 5) % 256
        g = (self.color[1] + 2) % 256
        b = (self.color[2] - 1) % 256

        self.color = [r, g, b]

        super().update()


class BouncingRainbow(BouncingBall, RainbowBall):
#     """
#     Ball that changes color and is affected by gravity
#     """
#     # TODO:

    def update(self):
        BouncingBall(self, self.position, self.velocity, self.color, self.radius, self.gravity)
        RainbowBall(self, self.position, self.velocity, self.color, self.radius)
        super().update()

class KineticBall(Ball):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     """
#     # TODO: update
    def __init__(self, ball_list, bounds, position, velocity, color, radius):
        self.ball_list = ball_list
        super().__init__(bounds, position, velocity, color, radius)
    
    def update(self):
        for ball in self.ball_list:
            if ball == self:
                continue

            else:
                distance = ball.position.distance_to(self.position)
                sumradius = self.radius + ball.radius

                if distance < sumradius:
                    print("Collision!")

        
        super().update()

# class KineticBouncing():
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """
    

# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """