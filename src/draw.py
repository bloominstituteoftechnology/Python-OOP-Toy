import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_balls(object_list):

    # #BouncingRainbows
    # bouncingrainbow = BouncingRainbow(SCREEN_SIZE, Vector2(100, 100), Vector2(3, 3), [255, 0, 255, .5], 20)
    # object_list.append(bouncingrainbow)

    # bouncingrainbow2 = BouncingRainbow(SCREEN_SIZE, Vector2(100, 100), Vector2(3, 3), [255, 0, 255, .5], 18)
    # object_list.append(bouncingrainbow2)

    # bouncingrainbow3 = BouncingRainbow(SCREEN_SIZE, Vector2(100, 100), Vector2(3, 3), [255, 0, 255, .5], 16)
    # object_list.append(bouncingrainbow3)

    # bouncingrainbow4 = BouncingRainbow(SCREEN_SIZE, Vector2(100, 100), Vector2(3, 3), [255, 0, 255, .5], 14)
    # object_list.append(bouncingrainbow4)

    # bouncingrainbow5 = BouncingRainbow(SCREEN_SIZE, Vector2(100, 100), Vector2(3, 3), [255, 0, 255, .5], 12)
    # object_list.append(bouncingrainbow5)

    # bouncingrainbow6 = BouncingRainbow(SCREEN_SIZE, Vector2(100, 100), Vector2(3, 3), [255, 0, 255, .5], 10)
    # object_list.append(bouncingrainbow6)

    # bouncingrainbow7 = BouncingRainbow(SCREEN_SIZE, Vector2(100, 100), Vector2(3, 3), [255, 0, 255, .5], 8)
    # object_list.append(bouncingrainbow7)

    # bouncingrainbow8 = BouncingRainbow(SCREEN_SIZE, Vector2(100, 100), Vector2(3, 3), [255, 0, 255, .5], 6)
    # object_list.append(bouncingrainbow8)

    # bouncingrainbow9 = BouncingRainbow(SCREEN_SIZE, Vector2(100, 100), Vector2(3, 3), [255, 0, 255, .5], 4)
    # object_list.append(bouncingrainbow9)

    # bouncingrainbow10 = BouncingRainbow(SCREEN_SIZE, Vector2(100, 100), Vector2(3, 3), [255, 0, 255, .5], 2)
    # object_list.append(bouncingrainbow10)


    #KineticBalls
    # kineticball1 = KineticBall(object_list, SCREEN_SIZE, Vector2(100, 300), Vector2(3, 0), [255, 0, 255], 15)
    # object_list.append(kineticball1)

    kineticball2 = KineticBall(object_list, SCREEN_SIZE, Vector2(500, 300), Vector2(-3, 0), [0, 0, 0], 15)
    object_list.append(kineticball2)

    # kineticball3 = KineticBall(object_list, SCREEN_SIZE, Vector2(200, 50), Vector2(0, 5), [0, 255, 255], 15)
    # object_list.append(kineticball3)

    kineticball4 = KineticBall(object_list, SCREEN_SIZE, Vector2(200, 400), Vector2(0, -2), [100, 100, 100], 15)
    object_list.append(kineticball4)

    # TODO: Create other ball types for testing
    
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
