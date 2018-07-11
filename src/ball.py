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
        # screen width
        new_pos = self.position + self.velocity
        x_edge = new_pos.x < 0 + self.radius or new_pos.x > \
            self.bounds[0] - self.radius
        y_edge = new_pos.y < 0 + self.radius or new_pos.y > \
            self.bounds[1] - self.radius
        if x_edge:
            self.velocity.x *= -1
        # screen height
        if y_edge:
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(
            self.position.x), int(self.position.y)], self.radius)


class BouncingBall(Ball):
    """
    ball effected by gravity
    """

    def update(self):
        if not self.position.y > self.bounds[1] - self.radius:
            self.velocity[1] += .98
        self.velocity *= .99
        super().update()


class RainbowBall(Ball):
    """
    Ball that changes colors
    """

    def update(self):
        self.color[0] = (self.color[0] + 3) % 256
        self.color[1] = (self.color[1] + 5) % 256
        self.color[2] = (self.color[2] + 7) % 256
        super().update()


class BouncingRainbow(BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """

    def update(self):
        RainbowBall.update(self)
        BouncingBall.update(self)


class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic
    circle collision
    """

    def __init__(self, bounds, position, velocity, color, radius,
                 other_shapes):
        self.other_shapes = [shape for shape in other_shapes if
                             hasattr(shape, "radius")]
        super().__init__(bounds, position, velocity, color, radius)

    def update(self):
        print(self.other_shapes)
        for shape in self.other_shapes:
            distance = (shape.position - self.position).length()
            if not shape == self and (distance <= self.radius + shape.radius):
                self_vec = self.velocity
                shape_vec = shape.velocity
                self.velocity -= (
                    (self_vec - shape_vec).dot(self.position - shape.position)
                    / (self.position - shape.position).length_squared()) * \
                    (self.position - shape.position)
                shape.velocity -= (
                    (shape_vec - self_vec).dot(shape.position - self.position)
                    / (shape.position - self.position).length_squared()) * \
                    (shape.position - self.position)

        super().update()

# class KineticBouncing(???):
#     """
#     A ball that collides with other collidable balls using simple elastic
#     circle collision
#     And is affected by gravity
#     """


# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """
