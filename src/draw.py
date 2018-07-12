import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [0, 0, 0 ]

def debug_create_balls(object_list):
    ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    object_list.append(ball)

    b_ball = RainbowBall(SCREEN_SIZE, Vector2(10, 50), Vector2(3, 3), [0, 255, 0], 10)
    object_list.append(b_ball)

    c_ball = BouncingBall(SCREEN_SIZE, Vector2(20, 10), Vector2(24, 10), [0, 255, 0], 10)
    object_list.append(c_ball)

    d_ball = KineticBall(SCREEN_SIZE, Vector2(35, 30), Vector2(7, 15), [0, 255, 0], 25)
    object_list.append(d_ball)

    e_ball = KineticBall(SCREEN_SIZE, Vector2(100, 100), Vector2(9, 11), [0, 255, 0], 25)
    object_list.append(e_ball)

    f_ball = KineticBouncing(SCREEN_SIZE, Vector2(45, 20), Vector2(9, 11), [0, 255, 0], 8)
    object_list.append(f_ball)

    g_ball = AllTheThings(SCREEN_SIZE, Vector2(65, 20), Vector2(9, 11), [0, 255, 0], 5)
    object_list.append(g_ball)

    # TODO: Create other ball types for testing
    
def debug_create_blocks(object_list):
    block = Block(SCREEN_SIZE, Vector2(100,100), 20, 20, [0,255,0])
    object_list.extend((block, ))

def set_collidables(object_list):
    for shape in object_list:
        if hasattr(shape, 'object_list'):
            shape.object_list = object_list

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = [] # list of objects of all types in the toy

    debug_create_balls(object_list)
    debug_create_blocks(object_list)
    set_collidables(object_list)

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
