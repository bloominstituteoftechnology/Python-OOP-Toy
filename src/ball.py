import math

from pygame.math import Vector2


class Ball:
    """
    base class for bouncing objects
    """
    def __init__(self, bounds, position, velocity, color, radius):
        self.bounds = bounds
        self.position = position
        self.velocity = velocity
        self.color = color
        self.radius = radius

    def update(self):
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius:  # screen width
            self.velocity.x *= -1
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius:  # screen height
                self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(
            screen, self.color, [int(self.position.x),
                                 int(self.position.y)], self.radius)

# class BouncingBall(???):


class BouncingBall(Ball):
    def update(self):
        if not self.position.y > self.bounds[1] - self.radius:
            self.velocity[1] += 0.8
        self.velocity *= 0.99
        super().update()

# class RainbowBall(???):


class RainbowBall(Ball):
    def update(self):
        r = (self.color[0] + 3) % 256
        g = (self.color[1] + 7) % 256
        b = (self.color[2] + 5) % 256
        self.color = [r, g, b]

        super().update()


# class BouncingRainbow(???):


class BouncingRainbow(BouncingBall, RainbowBall):
    def update(self):
        RainbowBall.update(self)
        BouncingBall.update(self)


class KineticBall(Ball):
    def __init__(self, bounds, position, velocity, color, radius, shapes):
        self.shapes = [shape for shape in shapes if hasattr(shape, "radius")]
        super().__init__(bounds, position, velocity, color, radius)

    def update(self):
        for shape in self.shapes:
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
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """


# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """
