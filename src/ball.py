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
        # bounce at edges.  TODO: Fix sticky edges
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius: 
            self.velocity.x *= -1  # screen width
        if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius:
            self.velocity.y *= -1  # screen height
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)


class BouncingBall(Ball):
    """
    ball effected by gravity
    """
    def __init__(self, bounds, position, velocity, color, radius):
        super().__init__(bounds, position, velocity, color, radius)
        self.max_velocity_y = math.fabs(velocity.y) + 10

    def update(self):
        # if falling increase v until it hits max else decrease v until it hits 0
        if self.velocity.y >= 0:  # 
            if self.velocity.y < self.max_velocity_y:
                self.velocity.y += 0.25
        else:
            if self.velocity.y != 0:
                self.velocity.y += 0.25
                
        super().update()


class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    def update(self):
        r = (self.color[0] + 1) % 255
        g = (self.color[1] + 5) % 255
        b = (self.color[2] + 10) % 255
        self.color = [r, g, b]

        super().update()


class BouncingRainbow(BouncingBall,RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    pass


class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    all_kinetic_balls = []

    def __init__(self, bounds, position, velocity, color, radius):
        super().__init__(bounds, position, velocity, color, radius)
        self.collided_with = None
        KineticBall.all_kinetic_balls.append(self)
    
    def detect_collision(self):
        for ball in KineticBall.all_kinetic_balls:
            if ball != self:
                # For this ball's center (P) and self's center (Q):
                # Collision if distance between P and Q = radius of P and radius of Q
                distance = ball.position.distance_to(self.position)
                sum_of_radiuses = ball.radius + self.radius
                if distance <= sum_of_radiuses:
                    self.collided_with = ball
                    return True
                else:
                    self.collided_with = None
                    return False

    def update(self):
        if self.detect_collision():
            b1 = self
            b2 = self.collided_with
            b1_mass = 1  # TODO - change mass
            b2_mass = 1  # basing off radius caused occasional collision issues
            
            collision_angle = math.atan2(b1.position.y - b2.position.y,
                                         b1.position.x - b2.position.x)

            # Need each ball's magnitude (speed) and angle of direction
            b1_magnitude = math.sqrt(b1.velocity.x**2 + b1.velocity.y**2)
            b2_magnitude = math.sqrt(b2.velocity.x**2 + b2.velocity.y**2)
            b1_direction = math.atan2(b1.velocity.y, b1.velocity.x)
            b2_direction = math.atan2(b2.velocity.y, b2.velocity.x)

            # Find initial velocity
            b1_initial_velocity_x = b1_magnitude*math.cos(b1_direction - collision_angle)
            b1_initial_velocity_y = b1_magnitude*math.sin(b1_direction - collision_angle)
            b2_initial_velocity_x = b2_magnitude*math.cos(b2_direction - collision_angle)
            b2_initial_velocity_y = b2_magnitude*math.sin(b2_direction - collision_angle)

            # Find final velocity
            b1_final_velocity_x = ((b1_mass-b2_mass)*b1_initial_velocity_x +
                                   (b2_mass+b2_mass)*b2_initial_velocity_x)/(b1_mass+b2_mass)
            b1_final_velocity_y = b1_initial_velocity_y
            b2_final_velocity_x = ((b1_mass+b1_mass)*b1_initial_velocity_x +
                                   (b2_mass-b1_mass)*b2_initial_velocity_x)/(b1_mass+b2_mass)
            b2_final_velocity_y = b2_initial_velocity_y

            # Convert angles
            self.velocity.x = math.cos(collision_angle)*b1_final_velocity_x + \
                math.cos(collision_angle+math.pi/2)*b1_final_velocity_y
            self.velocity.y = math.sin(collision_angle)*b1_final_velocity_x + \
                math.sin(collision_angle+math.pi/2)*b1_final_velocity_y
            self.collided_with.velocity.x = math.cos(collision_angle)*b2_final_velocity_x + \
                math.cos(collision_angle+math.pi/2)*b2_final_velocity_y
            self.collided_with.velocity.y = math.sin(collision_angle)*b2_final_velocity_x + \
                math.sin(collision_angle+math.pi/2)*b2_final_velocity_y

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
