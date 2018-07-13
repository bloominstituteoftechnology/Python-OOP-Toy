import pygame  #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]


def debug_create_balls(object_list):
    ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    object_list.append(ball)

    # TODO: Create other ball types for testing

    ball = BouncingBall(SCREEN_SIZE, Vector2(100, 100), Vector2(4, 4), [0, 0, 0], 10)
    object_list.append(ball)

    ball = RainbowBall(SCREEN_SIZE, Vector2(10, 10), Vector2(3, 3), [0, 0, 255], 10)
    object_list.append(ball)

    ball = BouncingRainbow(SCREEN_SIZE, Vector2(25, 25), Vector2(5, 5), [0, 255, 0], 10)
    object_list.append(ball)

    ball = KineticBall(object_list, SCREEN_SIZE, Vector2(33, 33), Vector2(3, 3), [122, 35, 45], 10)
    object_list.append(ball)

    ball = KineticBouncing(object_list, SCREEN_SIZE, Vector2(55, 55), Vector2(5, 5), [255, 0, 255], 10)
    object_list.append(ball)

    ball = AllTheThings(object_list, SCREEN_SIZE, Vector2(66, 66), Vector2(3, 3), [66, 66, 66], 10)
    print(type(ball))
    object_list.append(ball)

def debug_create_blocks(object_list):
    block = Block(SCREEN_SIZE, Vector2(100, 100), 20, 20, [0, 255, 0])
    object_list.extend((block, ))

    block = RainbowBlock(SCREEN_SIZE, Vector2(150, 100), 60, 30, [255, 255, 0])
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
            if event.type == pygame.KEYDOWN:  #TODO:  Get working
                if event.key == pygame.K_SPACE:
                    # TODO: Add behavior when button pressed
                    pass

        for obj in object_list:
            obj.update()

        # Draw Loop
        screen.fill(BACKGROUND_COLOR)
        for obj in object_list:
            obj.draw(screen, pygame)

        clock.tick(60)
        pygame.display.flip()

    # Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()
