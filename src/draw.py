import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_balls(object_list):
    ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    object_list.append(ball)

# first Vector 2 specifies coordinates on page (I think). Second vector 2 specifies speed. 
# [0,0,0] specifies RGB code and then the last entry is radius

    ball = Ball(SCREEN_SIZE, Vector2(10, 10), Vector2(10, 10), [0,255, 0], 10)
    object_list.append(ball)

    ball = RainbowBall(SCREEN_SIZE, Vector2(15, 20), Vector2(1, 1), [255, 0, 125], 15)
    object_list.append(ball)

    # TODO: Create other ball types for testing
    
def debug_create_blocks(object_list):
    block = Block(SCREEN_SIZE, Vector2(100,100), 20, 20, [0,255,0])
    object_list.extend((block, ))
    block = RainbowBlock(SCREEN_SIZE, Vector2(150,100), 50, 75, [0,0,255])
    object_list.extend((block, ))
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy

    ball = debug_create_balls(object_list)
    block = debug_create_blocks(object_list)
 
    done = False

    while not done: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_SPACE:
                    ball = debug_create_balls(object_list)
                    ball()
                elif event.key == pygame.K_RETURN:
                    block = debug_create_blocks(object_list)
                    block()
                else #TODO:
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
