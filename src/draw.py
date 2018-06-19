import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2
# from tkinter import *

from ball import *
from square import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    for i in range(5):
            ball = BouncingBall(SCREEN_SIZE, Vector2(random.randint(100, 400),
                                                    random.randint(100, 400)),
                                                    Vector2(random.random(), random.random()),
                                                    [255, 0, 0], 10)
            object_list.append(ball)

    # TODO: Create other ball types for testing
    square = FallingSq(SCREEN_SIZE, Vector2(50, 50), Vector2(0, 0), [0, 255, 0], 50, 50)
    object_list.append(square)
    square = FallingSq(SCREEN_SIZE, Vector2(600, 50), Vector2(0, 0), [0, 255, 0], 50, 50)
    object_list.append(square)
    square = FallingSq(SCREEN_SIZE, Vector2(300, 50), Vector2(0, 0), [0, 255, 0], 50, 50)
    object_list.append(square)

    square = RisingSq(SCREEN_SIZE, Vector2(200, 450), Vector2(0, 0), [0, 255, 0], 50, 50)
    object_list.append(square)

    square = BallingSq(SCREEN_SIZE, Vector2(400, 400), Vector2(0, 0), [0, 255, 0], 50, 50)
    object_list.append(square)
    

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy

    debug_create_objects(object_list)
 
    while True: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # Logic Loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  #TODO:  Get working
                if event.key == pygame.K_SPACE:
                    # TODO: Add behavior when button pressed
                    print('click')
                    ball = BouncingRainbow(SCREEN_SIZE, Vector2(random.randint(100, 400),
                                                    random.randint(100, 400)),
                                                    Vector2(random.random(), random.random()),
                                                    [255, 0, 0], 10)
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
