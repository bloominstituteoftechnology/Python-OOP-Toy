import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from rectangles import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    red = random.randrange(0, 255, 1)
    green = random.randrange(0, 255, 1)
    blue = random.randrange(0, 255, 1)
    height = random.randrange(0, 100, 1)
    width = random.randrange(0, 100, 1)
    startX = random.randrange(3, SCREEN_SIZE[0] - width, 1)
    startY = random.randrange(3, SCREEN_SIZE[1] - height, 1)
    speed = random.randrange(1, 10, 1)
    rect = Rectangle(SCREEN_SIZE, Vector2(startX, startY), Vector2(speed, speed), [red, green, blue], width, height)
    object_list.append(rect)

    # TODO: Create other rect types for testing

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = [] # list of objects of all types in the toy

    for i in range(25):
        debug_create_objects(object_list)

    for obj in object_list:
        obj.draw(screen, pygame)
    while True: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # Logic Loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  #TODO:  Get working
                if event.key == pygame.K_SPACE:
                    # TODO: Add behavior when button pressed
                    pass

        for rect in object_list:
            rect.update()

        # Draw Loop
        screen.fill(BACKGROUND_COLOR)
        for rect in object_list:
            rect.draw(screen, pygame)

        clock.tick(60)
        pygame.display.flip()

    #Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()