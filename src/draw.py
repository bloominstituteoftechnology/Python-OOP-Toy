import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from rectangle import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]


def debug_create_objects(object_list):
    for i in range(5):
        rectangle = BouncingRectangle(SCREEN_SIZE, Vector2(
            random.randint(100, 400), random.randint(100, 400)),
            Vector2(random.random(), random.random()), [0, 255, 0], 10, 10)
        object_list.append(rectangle)

    # TODO: Create other rectangle types for testing


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

        for rectangle in object_list:
            rectangle.update()

        # Draw Loop
        screen.fill(BACKGROUND_COLOR)
        for rectangle in object_list:
            rectangle.draw(screen, pygame)

        clock.tick(60)
        pygame.display.flip()

    # Close everything down
    pygame.quit()


if __name__ == "__main__":
    main()
