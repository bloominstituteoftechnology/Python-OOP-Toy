import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_balls(object_list):
    ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 10, 0], 10)
    bouncingBall = BouncingBall(SCREEN_SIZE, Vector2(50, 50), Vector2(2, 3), [1, 0, 255], 10)
    bouncingBall2 = BouncingBall2(SCREEN_SIZE, Vector2(50, 50), Vector2(2, 3), [12, 0, 255], 10)
    rainbowBall = RainbowBall(SCREEN_SIZE, Vector2(50, 50), Vector2(1, 3), [255, 10, 255], 10)
    bouncingRainbow = BouncingRainbow(SCREEN_SIZE, Vector2(50, 50), Vector2(0.5, 2), [0, 0, 255], 10) 
    object_list.append(ball)
    object_list.append(bouncingBall)
    object_list.append(bouncingBall2)
    object_list.append(rainbowBall)
    object_list.append(bouncingRainbow)
    kball = KineticBall(object_list, SCREEN_SIZE, Vector2(200, 100), Vector2(2, 2), [0, 255, 255], 30)
    object_list.append(kball)
    
    kball2 = KineticBall(object_list, SCREEN_SIZE, Vector2(120, 100), Vector2(3, 1), [0, 1, 25], 30)
    object_list.append(kball2)
    
    kball3 = KineticBall(object_list, SCREEN_SIZE, Vector2(400, 120), Vector2(3, 1), [90, 100, 250], 30)
    object_list.append(kball3)
    
    kball4 = KineticBouncing(object_list, SCREEN_SIZE, Vector2(500, 120), Vector2(3, 1), [90, 100, 250], 30)
    object_list.append(kball4)
    

    # TODO: Create other ball types for testing
    
def debug_create_blocks(object_list):
    block = Block(SCREEN_SIZE, Vector2(100,100), 20, 20, [0,255,0])
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

