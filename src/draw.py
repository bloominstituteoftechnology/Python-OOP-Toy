import pygame #TODO:  Fix intellisense
from random import randint

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_balls(object_list):
    # ball = Ball(SCREEN_SIZE, Vector2(50, 100), Vector2(3, 3), [255, 0, 0], 10)
    # object_list.append(ball)

    # bouncing_ball = BouncingBall(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 255], 10, -1)
    # object_list.append(bouncing_ball)

    # rainbow_ball = RainbowBall(SCREEN_SIZE, Vector2(50, 150), Vector2(3, 3), [255, 255, 0], 10)
    # object_list.append(rainbow_ball)

    # bouncing_rainbow = BouncingRainbow(SCREEN_SIZE, Vector2(50, 200), Vector2(3, 3), [255, 0, 255], 10, -1)
    # object_list.append(bouncing_rainbow)

    # kinetic_ball1 = KineticBall(SCREEN_SIZE, Vector2(randint(10, 630), randint(10, 470)), Vector2(3, 3), [255, 10, 255], 10, object_list)
    # object_list.append(kinetic_ball1)

    # kinetic_ball2 = KineticBall(SCREEN_SIZE, Vector2(randint(10, 630), randint(10, 470)), Vector2(3, 3), [255, 0, 0], 10, object_list)
    # object_list.append(kinetic_ball2)

    # kinetic_ball2 = KineticBall(SCREEN_SIZE, Vector2(randint(10, 630), randint(10, 470)), Vector2(3, 3), [255, 0, 0], 10, object_list)
    # object_list.append(kinetic_ball2)

    # kinetic_ball2 = KineticBall(SCREEN_SIZE, Vector2(randint(10, 630), randint(10, 470)), Vector2(3, 3), [255, 0, 0], 10, object_list)
    # object_list.append(kinetic_ball2)

    # kinetic_ball2 = KineticBall(SCREEN_SIZE, Vector2(randint(10, 630), randint(10, 470)), Vector2(3, 3), [255, 0, 0], 10, object_list)
    # object_list.append(kinetic_ball2)

    # kinetic_ball2 = KineticBall(SCREEN_SIZE, Vector2(randint(10, 630), randint(10, 470)), Vector2(3, 3), [255, 0, 0], 10, object_list)
    # object_list.append(kinetic_ball2)

    # ball = KineticBouncing(SCREEN_SIZE, Vector2(randint(10, 630), randint(10, 470)), Vector2(3, 3), [255, 0, 255], 10, -1, object_list)
    # object_list.append(ball)

    # ball = KineticBouncing(SCREEN_SIZE, Vector2(randint(10, 630), randint(10, 470)), Vector2(3, 3), [255, 0, 255], 10, -1, object_list)
    # object_list.append(ball)

    # ball = KineticBouncing(SCREEN_SIZE, Vector2(randint(10, 630), randint(10, 470)), Vector2(3, 3), [255, 0, 255], 10, -1, object_list)
    # object_list.append(ball)

    # ball = KineticBouncing(SCREEN_SIZE, Vector2(randint(10, 630), randint(10, 470)), Vector2(3, 3), [255, 0, 255], 10, -1, object_list)
    # object_list.append(ball)

    # ball = KineticBouncing(SCREEN_SIZE, Vector2(randint(10, 630), randint(10, 470)), Vector2(3, 3), [255, 0, 255], 10, -1, object_list)
    # object_list.append(ball)

    ball = AllTheThings(SCREEN_SIZE, Vector2(randint(10, 630), randint(10, 470)), Vector2(3, 3), [255, 0, 255], 10, -1, object_list)
    object_list.append(ball)

    ball = AllTheThings(SCREEN_SIZE, Vector2(randint(10, 630), randint(10, 470)), Vector2(3, 3), [255, 0, 255], 10, -1, object_list)
    object_list.append(ball)

    ball = AllTheThings(SCREEN_SIZE, Vector2(randint(10, 630), randint(10, 470)), Vector2(3, 3), [255, 0, 255], 10, -1, object_list)
    object_list.append(ball)

    ball = AllTheThings(SCREEN_SIZE, Vector2(randint(10, 630), randint(10, 470)), Vector2(3, 3), [255, 0, 255], 10, -1, object_list)
    object_list.append(ball)

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
 
    ##
    ## crazy while loop with nested for loops
    ##
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

        # loop through all the `ball` objects in `object_list`
        for ball in object_list:
            change_colors = getattr(ball, 'change_colors', None)
            
            ball.update()

            if callable(change_colors):
                ball.change_colors()

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
