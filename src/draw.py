import pygame
import random

from pygame.math import Vector2
from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_balls(object_list):
    ball = BouncingBall(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    object_list.append(ball)
    
def debug_create_blocks(object_list):
    block = Block(SCREEN_SIZE, Vector2(100,100), 20, 20, [0,255,0])
    object_list.extend((block, ))
  
def main():
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    object_list = []

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

        # Update items
        for obj in object_list:
            obj.update()
 
        # Draw items to buffer
        screen.fill(BACKGROUND_COLOR)
        for obj in object_list:
            obj.draw(screen, pygame)

        # Show buffer at x fps
        clock.tick(60)
        pygame.display.flip()
 
    pygame.quit()
 
if __name__ == "__main__":
    main()
