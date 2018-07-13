import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [1280, 960]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_balls(object_list):
    ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    object_list.append(ball)

# first Vector 2 specifies coordinates on page (I think). Second vector 2 specifies speed. 
# [0,0,0] specifies RGB code and then the last entry is radius

    ball = BouncingBall(SCREEN_SIZE, Vector2(10, 10), Vector2(10, 10), [0,255, 0], 10, .5)
    object_list.append(ball)

    ball = RainbowBall(SCREEN_SIZE, Vector2(15, 20), Vector2(1, 1), [255, 0, 125], 15)
    object_list.append(ball)

    ball = BouncingRainbow(SCREEN_SIZE, Vector2(25, 40), Vector2(3, 3), [255, 125, 125], 25, .1)
    object_list.append(ball)
    
    ball = KineticBall(object_list, SCREEN_SIZE, Vector2(200, 200), Vector2(10, 10), [0, 125, 125], 50)
    object_list.append(ball)

    # ball = KineticBouncing(object_list, SCREEN_SIZE, Vector2(225, 225), Vector2(5, 3), [255, 0, 125], 50)
    # object_list.append(ball)

    # ball = AllTheThings(object_list, SCREEN_SIZE, Vector2(50, 225), Vector2(2, 2), [125, 125, 125], 50)
    # object_list.append(ball)

    # TODO: ball = CollidingBall(object_list, SCREEN_SIZE, Vector2(50, 225), Vector2(2, 2), [125, 125, 125], 50)
    #object_list.append(ball) make a couple more colliding balls. If x position is in some kind of range, 
    # we know those balls are touching. We need a function that will update and handle the balls change.

    # 

    # TODO: Create other ball types for testing
    
def debug_create_blocks(object_list):
    # block = Block(SCREEN_SIZE, Vector2(100,100), 20, 20, [0,255,0])
    # object_list.extend((block, ))
    # block = RainbowBlock(SCREEN_SIZE, Vector2(150,100), 50, 75, [0,0,255])
    # object_list.extend((block, ))
    pass
  
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
                print("All Done!")
                break
            elif event.type == pygame.KEYDOWN:       
                if pygame.key:
                        done = True
                        event.type == pygame.QUIT
                        print('Really done!')
                        break

        for obj in object_list:
            obj.update()
 
        # Draw Loop
        screen.fill(BACKGROUND_COLOR)
        for obj in object_list:
            obj.draw(screen, pygame)
 
        clock.tick(30)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
