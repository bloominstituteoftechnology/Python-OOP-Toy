# import math

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
        # bounce at edges.
        # screen width
        next_pos = self.position + self.velocity
        x_left_edge_next = next_pos.x < 0 + self.radius
        x_right_edge_next = next_pos.x > self.bounds[0] - self.radius
        y_top_edge_next = next_pos.y < 0 + self.radius
        y_bottom_edge_next = next_pos.y > self.bounds[1] - self.radius
        if x_left_edge_next:
            self.position.x = self.radius * 2 - next_pos.x
            self.velocity.x *= -1
        elif x_right_edge_next:
            self.position.x = (self.bounds[0] - self.radius) * 2 - next_pos.x
            self.velocity.x *= -1
        else:
            self.position.x += self.velocity.x
        if y_top_edge_next:
            self.position.y = self.radius * 2 - next_pos.y
            self.velocity.y *= -1
        elif y_bottom_edge_next:
            self.position.y = (self.bounds[1] - self.radius) * 2 - next_pos.y
            self.velocity.y *= -1
        else:
            self.position.y += self.velocity.y

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(
            self.position.x), int(self.position.y)], self.radius)


class FrictionBall(Ball):
    def update(self):
        self.velocity *= .99
        super().update()


class BouncingBall(Ball):
    """
    ball effected by gravity
    """

    def update(self):
        next_pos = self.position + self.velocity
        if (self.position.y > self.bounds[1] - self.radius * 1.01 and
                abs(self.velocity.y) < self.radius / 32):
            self.position.y = self.bounds[1] - self.radius
            self.velocity.y = 0
        elif not (next_pos.y >= self.bounds[1] - self.radius and
                  self.velocity.y < self.radius):
            self.velocity.y += .98
        super().update()


class RainbowBall(Ball):
    """
    Ball that changes colors
    """

    def update(self):
        self.color[0] = (self.color[0] + 1) % 256
        self.color[1] = (self.color[1] + 3) % 256
        self.color[2] = (self.color[2] + 5) % 256
        super().update()


class BouncingRainbow(FrictionBall, BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity and friction
    """

    def update(self):
        FrictionBall.update(self)
        BouncingBall.update(self)
        RainbowBall.update(self)


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
        for shape in self.other_shapes:
            if shape == self:
                continue
            initial_dist = self.position - shape.position
            v_diff = self.velocity - shape.velocity

            product = initial_dist * v_diff
            s_diff = v_diff*v_diff
            if s_diff == 0:
                continue
            s_dist = initial_dist*initial_dist
            radii = self.radius + shape.radius
            t = (product * -1 - (product**2 - (s_diff) *
                                 (s_dist - radii**2))**.5)/(s_diff)
            if not isinstance(t, complex) and (t >= 0 and t < 1):
                self.position = self.position + self.velocity * t
                shape.position = shape.position + shape.velocity * t
                self_vec = Vector2(self.velocity.x, self.velocity.y)
                shape_vec = Vector2(shape.velocity.x, shape.velocity.y)

                self.velocity -= (2 * self.radius / (radii)) * (
                    (self_vec - shape_vec).dot(self.position - shape.position)
                    / (self.position - shape.position).length_squared()) * \
                    (self.position - shape.position)

                shape.velocity -= (2 * shape.radius / (radii)) * (
                    (shape_vec - self_vec).dot(shape.position - self.position)
                    / (shape.position - self.position).length_squared()) * \
                    (shape.position - self.position)

                self.position = self.position + self.velocity * (1 - t)
                shape.position = shape.position + shape.velocity * (1 - t)

        super().update()


class KineticBouncing(BouncingBall, KineticBall):
    """
    A ball that collides with other collidable balls using simple elastic
    circle collision
    And is affected by gravity
    """

    def update(self):
        BouncingBall.update(self)
        KineticBall.update(self)


class GravityBall(KineticBall):
    def update(self):
        for shape in self.other_shapes:
            distance = self.position.distance_to(shape.position)
            power = (self.radius * shape.radius) / distance ** 2


# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """
