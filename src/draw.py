import pygame
import sys

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
from block import Block, RainbowBlock

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]


def create_balls(object_list):
    ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    object_list.append(ball)

    rainbowball = RainbowBall(
        SCREEN_SIZE, Vector2(50, 50), Vector2(3, 6), [255, 255, 0], 40
    )
    object_list.append(rainbowball)

    bouncingball = BouncingBall(
        SCREEN_SIZE, Vector2(50, 50), Vector2(3, 6), [255, 255, 0], 20
    )
    object_list.append(bouncingball)

    bouncingrain = BouncingRainbow(
        SCREEN_SIZE, Vector2(30, 60), Vector2(2, 12), [255, 255, 0], 30
    )
    object_list.append(bouncingrain)

    orbitalball = OrbitalBall(
        object_list, SCREEN_SIZE, Vector2(30, 60), Vector2(2, 12), [255, 0, 0], 5
    )
    object_list.extend((orbitalball,))

    kinetic = KineticBall(
        object_list, SCREEN_SIZE, Vector2(30, 60), Vector2(2, 12), [255, 0, 200], 20
    )
    object_list.extend((kinetic,))

    kinetic2 = KineticBall(
        object_list, SCREEN_SIZE, Vector2(30, 60), Vector2(5, 10), [255, 0, 200], 20
    )
    object_list.extend((kinetic2,))

    kineticball = KineticBouncing(
        object_list, SCREEN_SIZE, Vector2(30, 60), Vector2(5, 10), [138, 0, 255], 20
    )
    object_list.extend((kineticball,))

    allthethings = AllTheThings(
        object_list, SCREEN_SIZE, Vector2(30, 60), Vector2(5, 10), [0, 255, 0], 20
    )
    object_list.extend((allthethings,))
    # TODO: Create other ball types for testing


def create_blocks(object_list):
    block = Block(SCREEN_SIZE, Vector2(100, 100), 20, 20, [0, 255, 0])
    object_list.extend((block,))

    block = RainbowBlock(SCREEN_SIZE, Vector2(100, 100), 20, 20, [0, 255, 0])
    object_list.extend((block,))


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy

    create_balls(object_list)
    create_blocks(object_list)

    while True:  # TODO:  Create more elegant condition for loop
        print("object_list", object_list)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                for item in object_list:
                    if hasattr(item, "radius"):
                        continue
                    # y = item.velocity.y
                    # x = item.velocity.x
                    # if event.key == pygame.K_UP:
                    #     if item.velocity.y == 0:
                    #         item.velocity.y = -abs(item.velocity.x)
                    #     else:
                    #         item.velocity.y = 0 - abs(y)
                    #     item.velocity.x = 0
                    # if event.key == pygame.K_DOWN:
                    #     if item.velocity.y == 0:
                    #         item.velocity.y = abs(item.velocity.x)
                    #     else:
                    #         item.velocity.y = abs(y)
                    #     item.velocity.x = 0
                    # if event.key == pygame.K_RIGHT:
                    #     if item.velocity.x == 0:
                    #         item.velocity.x = abs(item.velocity.y)
                    #     else:
                    #         item.velocity.x = abs(x)
                    #     item.velocity.y = 0
                    # if event.key == pygame.K_LEFT:
                    #     if item.velocity.x == 0:
                    #         item.velocity.x = -abs(item.velocity.y)
                    #     else:
                    #         item.velocity.x = 0 - abs(x)
                    #     item.velocity.y = 0

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
