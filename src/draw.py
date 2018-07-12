import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_balls(object_list):
    ball = Ball(SCREEN_SIZE, Vector2(150, 50), Vector2(5, 3), [55, 50, 0], 10)

    bouncingBall1 = BouncingBall(SCREEN_SIZE, Vector2(150, 100), Vector2(20, 10), [255, 0, 0], 20, 100)
    bouncingBall2 = BouncingBall(SCREEN_SIZE, Vector2(50, 50), Vector2(50, 5), [0, 255, 0], 50, 50)

    rainbowBall = RainbowBall(SCREEN_SIZE, Vector2(150, 250), Vector2(3, 5), [55, 20, 0], 20)

    bouncingRainbow1 = BouncingRainbow(SCREEN_SIZE, Vector2(150, 250), Vector2(3, 5), [0, 50, 20], 30, 100)
    bouncingRainbow2 = BouncingRainbow(SCREEN_SIZE, Vector2(150, 250), Vector2(3, 5), [0, 10, 10], 30, 200)

    object_list.append(ball)
    object_list.append(bouncingBall1)
    object_list.append(bouncingBall2)

    object_list.append(rainbowBall)

    object_list.append(bouncingRainbow1)
    object_list.append(bouncingRainbow2)



    # TODO: Create other ball types for testing
    
def debug_create_blocks(object_list):
    block = Block(SCREEN_SIZE, Vector2(100,100), 20, 20, [0,255,0])
    object_list.extend((block, ))

def debug_start_game(object_list):
    debug_create_balls(object_list)
    debug_create_blocks(object_list)
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy

    while True: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:  #TODO:  Get working
                if event.key == pygame.K_SPACE:
                    # TODO: Add behavior when button pressed
                    print(event)
                if event.key == pygame.K_s:
                    # TODO: Add behavior when button pressed
                    debug_start_game(object_list)
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
