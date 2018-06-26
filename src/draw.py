# 1.  Get what we did in class working
# 2.  Experiment a bit on your on
# 3.  Make a new file and base class that draws rectangles
# 4.  Experiment with those
# 5.  VERY HARD STRETCH GOAL:  Implement simple elastic collision with the balls
import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from rectangles import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]


def debug_create_objects(object_list):
    for i in range(4):
        # ball = Ball(SCREEN_SIZE, Vector2(50 + i*21, 50+i*41), Vector2(3, 3), [255, 0, 0], 10)
        # bBall = BouncingBall(SCREEN_SIZE, Vector2(150 + i * 14, 150 + i * 25), Vector2(4, 4), [0, 0, 255], 10)

        ball = Ball(SCREEN_SIZE, Vector2(random.randint(10, 400),
                                         random.randint(10, 300)), Vector2(3 + 2, 3 + 2), [255, 0, 0], 10)
        bBall = BouncingBall(SCREEN_SIZE, Vector2(random.randint(
            50, 400), random.randint(60, 140)), Vector2(4, 4), [0, 0, 255], 10)
        rBall = RainbowBall(SCREEN_SIZE, Vector2(random.randint(
            150, 200), random.randint(160, 240)), Vector2(5, 2), [0, 255, 0], 10)
        rbBall = BouncingRainbow(SCREEN_SIZE, Vector2(random.randint(
            10, 200), random.randint(10, 24)), Vector2(1, 2), [134, 55, 100], 10)

        rec = Rectangle(SCREEN_SIZE, Vector2(random.randint(70, 300),
                                             random.randint(40, 100)), Vector2(1, 2), [22, 214, 40], 30, 50)

        object_list.append(ball)
        object_list.append(bBall)
        object_list.append(rBall)
        object_list.append(rbBall)
        object_list.append(rec)

    # TODO: Create other ball types for testing


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy

    debug_create_objects(object_list)

    while True:  # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # Logic Loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # TODO:  Get working
                if event.key == pygame.K_SPACE:
                    # TODO: Add behavior when button pressed
                    pass

        for ball in object_list:
            ball.update()

        # Draw Loop
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)

        clock.tick(60)
        pygame.display.flip()

    # Close everything down
    pygame.quit()


if __name__ == "__main__":
    main()
