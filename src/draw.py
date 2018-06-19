import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]
randX1 = random.randint(1,639)
randY1 = random.randint(1,479)

def debug_create_objects(object_list):
    ball = Ball(SCREEN_SIZE, Vector2(25,50), Vector2(3, 3), [255, 0, 0], 10)
    ball1= Ball(SCREEN_SIZE, Vector2(randX1,randY1), Vector2(3, 3), [0, 255, 0], 10)
    object_list.append(ball)
    object_list.append(ball1)

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