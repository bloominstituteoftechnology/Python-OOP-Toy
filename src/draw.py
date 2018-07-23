import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_balls(object_list):
    # ball1 = BouncingBall(SCREEN_SIZE, Vector2(50, 50), Vector2(-3, -3), [255, 0, 0], 10)
    # object_list.append(ball1)

    # ball2 = RainbowBall(SCREEN_SIZE, Vector2(20, 60), Vector2(-3, -3), [255, 0, 0], 10)
    # object_list.append(ball2)

    ball3 = BouncingRainbow(SCREEN_SIZE, Vector2(100, 30), Vector2(-3, -3), [255, 0, 0], 10)
    object_list.append(ball3)

    # TODO: Create other ball types for testing
    
def debug_create_blocks(object_list):
    block = Block(SCREEN_SIZE, Vector2(50,100), 100, 30, [0,255,0])
    object_list.extend((block, ))

    block1 = Block(SCREEN_SIZE, Vector2(100,50), 20, 20, [0,255,0])
    object_list.extend((block1, ))
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy

    debug_create_balls(object_list)
    debug_create_blocks(object_list)
 
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
