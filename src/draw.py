import pygame  # TODO:  Fix intellisense

import pygame  # TODO:  Fix intellisense
from ball import *
from block import *
from pygame.math import Vector2

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_balls(object_list):

    ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    object_list.append(ball)

    # TODO: Create other ball types for testing
    


    block = Block(SCREEN_SIZE, Vector2(100,100), 20, 20, [0,255,0])
    block = Block(SCREEN_SIZE, Vector2(100, 100), 20, 20, [0, 255, 0])
    object_list.extend((block,))


    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 

    clock = pygame.time.Clock()
 

    object_list = []  # list of objects of all types in the toy
    debug_create_balls(object_list)
    debug_create_blocks(object_list)
 

    while True:  # TODO:  Create more elegant condition for loop
            if event.type == pygame.QUIT:
                pygame.quit()
        # Logic Loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  #TODO:  Get working
            if event.type == pygame.KEYDOWN:  # TODO:  Get working
                    # TODO: Add behavior when button pressed
                    pass

        for ball in object_list:
            ball.update()
 

        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)
 

        pygame.display.flip()
 

    pygame.quit()
 


    main()
