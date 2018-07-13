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
    
    bouncing_ball = BouncingBall(SCREEN_SIZE, Vector2(100,100), Vector2(3,0), [50,50,50],8)
    object_list.append(bouncing_ball)

    rainbow_ball = RainbowBall(SCREEN_SIZE, Vector2(400,300), Vector2(3,-2), [57,122,242], 8)
    object_list.append(rainbow_ball)

    bouncing_rainbow = BouncingRainbow(SCREEN_SIZE, Vector2(100, 100), Vector2(2,2), [255, 0, 0], 7)
    object_list.append(bouncing_rainbow)
    
    kinetic_ball = KineticBall(SCREEN_SIZE, Vector2(200,100), Vector2(2,0), [0, 255, 0], 30)
    object_list.append(kinetic_ball)
    # kinetic_bouncing = KineticBouncing(SCREEN_SIZE, Vector2(45,30), Vector2(9,10), [0,255,0], 8)
    # object_list.append(kinetic_bouncing)

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
