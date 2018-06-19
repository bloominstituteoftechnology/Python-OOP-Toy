import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from rect import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [0, 0, 0]

def debug_create_objects(object_list):
    # QUESTION: Looking at the class `Ball` parameters, I see 6, but only see 5 values passed here?
    # # Where/What is "self"???
    for i in range(5):
        rect = BouncingRainbow(SCREEN_SIZE, Vector2(random.randint(100,400),
                                                 random.randint(100,400)), 
                                                 Vector2((2 + random.random())%3, 
                                                         (2 + random.random())%3),
                                                         [255, 165, 0], 50, 80) # This is the constructor!
        object_list.append(rect)

    # TODO: Create other rect types for testing
  
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

        for rect in object_list:
            rect.update()
 
        # Draw Loop
        screen.fill(BACKGROUND_COLOR)
        for rect in object_list:
            rect.draw(screen, pygame)
 
        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
