import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [1280, 960]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_balls(ball_list):
    ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    ball_list.append(ball)

# first Vector 2 specifies coordinates on page (I think). Second vector 2 specifies speed. 
# [0,0,0] specifies RGB code and then the last entry is radius

    ball = BouncingBall(SCREEN_SIZE, Vector2(10, 10), Vector2(10, 10), [0,255, 0], 10, .5)
    ball_list.append(ball)

    ball = RainbowBall(SCREEN_SIZE, Vector2(15, 20), Vector2(1, 1), [255, 0, 125], 15)
    ball_list.append(ball)

    ball = BouncingRainbow(SCREEN_SIZE, Vector2(25, 40), Vector2(3, 3), [255, 125, 125], 25, .1)
    ball_list.append(ball)
    
    ball = KineticBall(ball_list, SCREEN_SIZE, Vector2(200, 200), Vector2(10, 10), [0, 125, 125], 50)
    ball_list.append(ball)

    # ball = KineticBouncing(object_list, SCREEN_SIZE, Vector2(225, 225), Vector2(5, 3), [255, 0, 125], 50)
    # object_list.append(ball)

    # ball = AllTheThings(object_list, SCREEN_SIZE, Vector2(50, 225), Vector2(2, 2), [125, 125, 125], 50)
    # object_list.append(ball)

    # TODO: ball = CollidingBall(object_list, SCREEN_SIZE, Vector2(50, 225), Vector2(2, 2), [125, 125, 125], 50)
    #object_list.append(ball) make a couple more colliding balls. If x position is in some kind of range, 
    # we know those balls are touching. We need a function that will update and handle the balls change.

    # 

    # TODO: Create other ball types for testing
    
def debug_create_blocks(block_list):
    a = random.randint(0, 1280)
    b = random.randint(0, 960)
    c = random.randint(0, 1280)
    d = random.randint(0, 960)
    block = Block(SCREEN_SIZE, Vector2(a,b), Vector2(10, 10), random.randint(30, 50), random.randint(15, 60), [0,255,0])
    block_list.append(block)
    block = RainbowBlock(SCREEN_SIZE, Vector2(c,d), Vector2(3, 3), random.randint(70, 90), random.randint(15, 50), [0,0,255])
    block_list.append(block)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    block_list = [] # list of objects of all types in the toy
    ball_list = []
    done = False

    while not done: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
                print("All Done!")
            elif event.type == pygame.KEYDOWN:       
                if event.key == pygame.K_ESCAPE:
                    done = True
                    print("For real this time...done.")
                elif event.key == pygame.K_SPACE:
                    debug_create_balls(ball_list)
                    print("Was there a ball created?")
                elif event.key == pygame.K_RETURN:
                    debug_create_blocks(block_list)
                    print("Was there a set of new blocks created?")
                
            else:
                continue
                

        for obj in ball_list:
            obj.update()
        for obj in block_list:
            obj.update()
 
        # Draw Loop
        screen.fill([0, 0, 0])
        for obj in ball_list:
            obj.draw(screen, pygame)
        for obj in block_list:
            obj.draw(screen, pygame)
 
        clock.tick(30)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
