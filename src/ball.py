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
        x_edge_exact = self.position.x == self.radius or \
            self.position.x == self.bounds[0] - self.radius
        y_edge_exact = self.position.y == self.radius or \
            self.position.y == self.bounds[1] - self.radius
        print(x_edge_exact)
        if x_edge_exact:
            print("HEEEEEEEEEEEEEEEEY!!!!!!!!!!!!")
            self.velocity.x *= -1
        if y_edge_exact:
            self.velocity.y *= -1
        if not (x_edge_exact or y_edge_exact):
            next_pos = self.position + self.velocity
            x_left_edge_next = next_pos.x < 0 + self.radius
            x_right_edge_next = next_pos.x > self.bounds[0] - self.radius
            y_top_edge_next = next_pos.y < 0 + self.radius
            y_bottom_edge_next = next_pos.y > self.bounds[1] - self.radius
            if x_left_edge_next:
                print("YOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!!!!!!!")
                self.position.x = self.radius
            elif x_right_edge_next:
                self.position.x = self.bounds[0] - self.radius
            else:
                self.position.x += self.velocity.x
            if y_top_edge_next:
                self.position.y = self.radius
            elif y_bottom_edge_next:
                self.position.y = self.bounds[1] - self.radius
            else:
                self.position.y += self.velocity.y
        else:
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
        next_pos = self.position + self.velocity
        if not next_pos.y >= self.bounds[1] - self.radius - 1:
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
            next_pos_self = self.position + self.velocity
            next_pos_shape = shape.position + shape.velocity
            distance = (next_pos_shape - next_pos_self).length()
            if (not shape == self) and (distance <= self.radius + shape.radius):
                self_vec = Vector2(self.velocity.x, self.velocity.y)
                shape_vec = Vector2(shape.velocity.x, shape.velocity.y)
                self.velocity -= (
                    (self_vec - shape_vec).dot(next_pos_self - next_pos_shape)
                    / (next_pos_self - next_pos_shape).length_squared()) * \
                    (next_pos_self - next_pos_shape)
                shape.velocity -= (
                    (shape_vec - self_vec).dot(next_pos_shape - next_pos_self)
                    / (next_pos_shape - next_pos_self).length_squared()) * \
                    (next_pos_shape - next_pos_self)

        super().update()


class KineticBouncing(KineticBall, BouncingBall):
    """
    A ball that collides with other collidable balls using simple elastic
    circle collision
    And is affected by gravity
    """

    def update(self):
        KineticBall.update(self)
        BouncingBall.update(self)


# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """
