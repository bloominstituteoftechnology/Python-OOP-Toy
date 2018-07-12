import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_balls(object_list):
    ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    ball2 = BouncingBall(SCREEN_SIZE, Vector2(20, 60), Vector2(2, 2), [107,142,35], 10)
    ball3 = RainbowBall(SCREEN_SIZE, Vector2(30, 80), Vector2(4, 4), [255, 0, 0], 10)
    ball4 = BouncingRainbow(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    ball5 = KineticBall(object_list, SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [0, 0, 128], 10)
    # ball6 = KineticBouncing(SCREEN_SIZE, Vector2(20, 350), Vector2(1, 5), [105, 105, 105], 10)
    # ball7 = AllTheThings(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    object_list.extend([ball, ball2, ball3, ball4, ball5])
    
def debug_create_blocks(object_list):
    # block = Block(SCREEN_SIZE, Vector2(100,100), 20, 20, [0,255,0])
    # object_list.extend((block, ))
    pass
  
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
