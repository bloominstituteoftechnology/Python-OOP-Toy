import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [1024, 768]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_balls(object_list):
    a_ball = KineticBouncing(SCREEN_SIZE, Vector2(10, 10), Vector2(1, 1), [255, 0, 0], 10)
    b_ball = KineticBall(SCREEN_SIZE, Vector2(50, 10), Vector2(1, 1), [0, 255, 0], 25)
    c_ball = KineticBouncing(SCREEN_SIZE, Vector2(100, 10), Vector2(1, 1), [255, 0, 0], 25)
    d_ball = KineticBall(SCREEN_SIZE, Vector2(150, 10), Vector2(1, 1), [0, 255, 0], 10)
    e_ball = AllTheThings(SCREEN_SIZE, Vector2(200, 10), Vector2(1, 1), [255, 0, 0], 50)
    object_list.append(a_ball)
    object_list.append(b_ball)
    object_list.append(c_ball)
    object_list.append(d_ball)
    object_list.append(e_ball)
    # TODO: Create other ball types for testing

def set_collidables(object_list):
    for shape in object_list:
        if hasattr(shape, 'collidable'):
            shape.entities = object_list

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
