import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]
  
def main():
    pygame.init()
 
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy

    ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    object_list.append(ball)

    bouncing_ball = BouncingBall(SCREEN_SIZE, Vector2(100, 100), Vector2(3, 0),
                                    [0, 0, 255], 8)
    object_list.append(bouncing_ball)

    rainbow_ball = RainbowBall(SCREEN_SIZE, Vector2(400, 300), Vector2(3, -2),
                                    [0, 255, 0], 8)
    object_list.append(rainbow_ball)

    bouncing_rainbow_ball = BouncingRainbow(SCREEN_SIZE, Vector2(300, 150),
                                    Vector2(-4, 0), [0, 255, 0], 8)
    object_list.append(bouncing_rainbow_ball)
 
    while True: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        # Logic Updates
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  #TODO:  Get working
                if event.key == pygame.K_SPACE:
                    # ball = Ball(SCREEN_SIZE, 50, 50, 3, 3, [255, 0, 0], 10)
                    # object_list.append(ball)
                    pass

        for ball in object_list:
            ball.update()
 
        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)
 
        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
