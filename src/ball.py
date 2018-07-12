import math

from pygame.math import Vector2


class Ball:
    """
    base class for bouncing objects
    """

    def __init__(self, bounds, position, velocity, color, radius):
        self.bounds = bounds  # screen size
        self.position = position  # vector2
        self.velocity = velocity  # vector2
        self.color = color  # rgb
        self.radius = radius  # int

    def update(self):
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
        pygame.draw.circle(
            screen,
            self.color,
            [int(self.position.x), int(self.position.y)],
            self.radius,
        )


# class BouncingBall(???):


class BouncingBall(Ball):
    def update(self):
        next_position = self.position + self.velocity

        if (
            self.position.y > self.bounds[1] - self.radius * 1.001
            and abs(self.velocity.y) < self.radius / 16
        ):
            self.position.y = self.bounds[1] - self.radius
            self.velocity.y = 0

        elif math.isclose(next_position.y, (self.bounds[1] - (self.radius))):
            self.velocity.y = 0
            self.position.y = self.bounds[1]
        else:
            self.velocity.y += .98
        self.velocity *= .99
        super().update()


class RainbowBall(Ball):
    def update(self):
        r = (self.color[0] + 3) % 256
        g = (self.color[1] + 7) % 256
        b = (self.color[2] + 5) % 256
        self.color = [r, g, b]

        super().update()


class BouncingRainbow(BouncingBall, RainbowBall):
    def update(self):
        BouncingBall.update(self)
        RainbowBall.update(self)


class OrbitalBall(Ball):
    def __init__(self, shapes, bounds, position, velocity, color, radius):
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
                    / (self.position - shape.position).length_squared()
                ) * (self.position - shape.position)
                shape.velocity -= (
                    (shape_vec - self_vec).dot(shape.position - self.position)
                    / (shape.position - self.position).length_squared()
                ) * (shape.position - self.position)
        super().update()


class KineticBall(Ball):
    def __init__(self, shapes, bounds, position, velocity, color, radius):
        self.shapes = [shape for shape in shapes if hasattr(shape, "radius")]
        super().__init__(bounds, position, velocity, color, radius)

    def update(self):
        for shape in self.shapes:
            if shape == self:
                continue
            initial_dist = self.position - shape.position
            v_diff = self.velocity - shape.velocity

            product = initial_dist * v_diff
            s_diff = v_diff * v_diff
            if s_diff == 0:
                continue
            s_dist = initial_dist * initial_dist
            radii = self.radius + shape.radius
            t = (
                product * -1 - (product ** 2 - (s_diff) * (s_dist - radii ** 2)) ** .5
            ) / (s_diff)
            if not isinstance(t, complex) and (t >= 0 and t < 1):
                self.position = self.position + self.velocity * t
                shape.position = shape.position + shape.velocity * t
                self_vec = Vector2(self.velocity.x, self.velocity.y)
                shape_vec = Vector2(shape.velocity.x, shape.velocity.y)
                self.velocity -= (
                    (2 * self.radius / (radii))
                    * (
                        (self_vec - shape_vec).dot(self.position - shape.position)
                        / (self.position - shape.position).length_squared()
                    )
                    * (self.position - shape.position)
                )
                shape.velocity -= (
                    (2 * shape.radius / (radii))
                    * (
                        (shape_vec - self_vec).dot(shape.position - self.position)
                        / (shape.position - self.position).length_squared()
                    )
                    * (shape.position - self.position)
                )

                self.position += self.velocity * 2
                shape.position += shape.velocity * 2
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
