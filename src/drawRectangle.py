import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from rectangle import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]



def debug_create_objects(object_list):
    rectangle = Rectangle(SCREEN_SIZE,  [255, 0, 0], (3, 3), 100, 50)
    object_list.append(rectangle)



def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy

    debug_create_objects(object_list)
 
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