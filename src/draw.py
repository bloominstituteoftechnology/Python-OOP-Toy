import pygame  # TODO:  Fix intellisense
# import random

from pygame.math import Vector2

from ball import Ball, RainbowBall, BouncingBall, BouncingRainbow, \
    KineticBall, KineticBouncing, FrictionBall
from block import Block

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]


def debug_create_balls(object_list):
    ball = Ball(SCREEN_SIZE, Vector2(50, 500), Vector2(0, 10), [255, 0, 0], 10)
    object_list.append(ball)
    ball = RainbowBall(SCREEN_SIZE, Vector2(25, 25), Vector2(3, 2),
                       [0, 255, 0], 10)
    object_list.append(ball)
    ball = BouncingBall(SCREEN_SIZE, Vector2(500, 20), Vector2(10, 4),
                        [0, 255, 0], 15)
    object_list.append(ball)
    ball = FrictionBall(SCREEN_SIZE, Vector2(500, 20), Vector2(10, 4),
                        [0, 0, 0], 15)
    object_list.append(ball)
    ball = BouncingRainbow(SCREEN_SIZE, Vector2(100, 300), Vector2(-10, 2),
                           [0, 255, 0], 15)
    object_list.append(ball)
    ball = KineticBall(SCREEN_SIZE, Vector2(200, 200), Vector2(0, 10),
                       [0, 255, 255], 15, object_list)
    object_list.append(ball)
    ball = KineticBouncing(SCREEN_SIZE, Vector2(23, 15), Vector2(-5, 3),
                           [122, 122, 122], 10, object_list)
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

        for shape in object_list:
            shape.update()

        # Draw Loop
        screen.fill(BACKGROUND_COLOR)
        for shape in object_list:
            shape.draw(screen, pygame)

        clock.tick(60)
        pygame.display.flip()

    # Close everything down
    pygame.quit()


if __name__ == "__main__":
    main()
