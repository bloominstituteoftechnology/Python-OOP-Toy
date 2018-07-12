import pygame

# TODO:  Fix intellisense
# import random

from pygame.math import Vector2

from ball import (
    Ball,
    RainbowBall,
    BouncingBall,
    BouncingRainbow,
    OrbitalBall,
    KineticBall,
    KineticBouncing,
    AllTheThings,
)
from block import Block

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]


def create_balls(object_list):
    ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    object_list.append(ball)

    ball = RainbowBall(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 6), [255, 255, 0], 40)
    object_list.extend((ball,))

    ball = BouncingBall(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 6), [255, 255, 0], 20)
    object_list.extend((ball,))

    ball = BouncingRainbow(
        SCREEN_SIZE, Vector2(30, 60), Vector2(2, 12), [255, 255, 0], 30
    )
    object_list.extend((ball,))

    ball = OrbitalBall(
        object_list, SCREEN_SIZE, Vector2(30, 60), Vector2(2, 12), [255, 0, 0], 5
    )
    object_list.extend((ball,))

    ball = KineticBall(
        object_list, SCREEN_SIZE, Vector2(30, 60), Vector2(2, 12), [255, 0, 200], 20
    )
    object_list.extend((ball,))

    ball = KineticBall(
        object_list, SCREEN_SIZE, Vector2(30, 60), Vector2(5, 10), [255, 0, 200], 20
    )
    object_list.extend((ball,))

    ball = KineticBouncing(
        object_list, SCREEN_SIZE, Vector2(30, 60), Vector2(5, 10), [138, 0, 255], 20
    )
    object_list.extend((ball,))

    ball = AllTheThings(
        object_list, SCREEN_SIZE, Vector2(30, 60), Vector2(5, 10), [0, 255, 0], 20
    )
    object_list.extend((ball,))
    # TODO: Create other ball types for testing


def create_blocks(object_list):
    block = Block(SCREEN_SIZE, Vector2(100, 100), 20, 20, [0, 255, 0])
    object_list.extend((block,))


def main():
    done = False
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy

    create_balls(object_list)
    create_blocks(object_list)

    while not done:  # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
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
