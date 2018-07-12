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

    # TODO: Create other ball types for testing

    ball = BouncingBall(SCREEN_SIZE, Vector2(60, 60), Vector2(4, 4), [255, 0, 0], 15)
    object_list.append(ball)

    ball = RainbowBall(SCREEN_SIZE, Vector2(55, 55), Vector2(2, 2), [255, 0, 0], 10)
    object_list.append(ball)

    ball = BouncingRainbow(SCREEN_SIZE, Vector2(58, 58), Vector2(3.5, 3.5), [255, 0, 0], 15)
    object_list.append(ball)

    ball = KineticBall(object_list, SCREEN_SIZE, Vector2(200, 200), Vector2(2, 10), [0, 255, 255], 30)
    object_list.append(ball)

    ball = KineticBouncing(object_list, SCREEN_SIZE, Vector2(300, 300), Vector2(3, 3), [0, 255, 255], 20)
    object_list.append(ball)

    ball = AllTheThings(object_list, SCREEN_SIZE, Vector2(100, 100), Vector2(4, 4), [0, 255, 255], 20)
    object_list.append(ball)

def debug_create_blocks(object_list):
    block = Block(SCREEN_SIZE, Vector2(100,100), 20, 20, [0,255,0])
    object_list.extend((block, ))

    block = RainbowBlock(SCREEN_SIZE, Vector2(200,100), 100, 20, [0,255,0])
    object_list.extend((block, ))
  
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
