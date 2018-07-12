import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]


def debug_create_balls(object_list):
    ball = Ball(SCREEN_SIZE, Vector2(50, 50),
                Vector2(3, 3), [255, 0, 0], 10)
    object_list.append(ball)

    ball = RainbowBall(SCREEN_SIZE, Vector2(20, 350),
                       Vector2(1, 5), [255, 0, 0], 10)
    object_list.append(ball)

    ball = BouncingBall(SCREEN_SIZE, Vector2(30, 200),
                        Vector2(5, 5), [0, 255, 0], 10)
    object_list.append(ball)

    ball = BouncingRainbow(SCREEN_SIZE, Vector2(40, 250),
                           Vector2(7, 7), [0, 255, 255], 10)
    object_list.append(ball)

    ball = KineticBall(object_list, SCREEN_SIZE, Vector2(
        200, 100), Vector2(2, 0), [0, 255, 255], 30)
    object_list.append(ball)

    ball = KineticBouncing(object_list, SCREEN_SIZE, Vector2(
        300, 400), Vector2(8, 8), [200, 255, 255], 30)
    object_list.append(ball)

    ball = AllTheThings(object_list, SCREEN_SIZE, Vector2(
        200, 100), Vector2(9, 9), [255, 255, 255], 30)
    object_list.append(ball)

    # TODO: Create other ball types for testing


def debug_create_blocks(object_list):
    block = Block(SCREEN_SIZE, Vector2(100, 100), 20, 20, [0, 255, 0])
    object_list.extend((block, ))


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy

    debug_create_balls(object_list)
    debug_create_blocks(object_list)

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
        # pygame.display.get_caption()

    # Close everything down
    pygame.quit()


if __name__ == "__main__":
    main()
