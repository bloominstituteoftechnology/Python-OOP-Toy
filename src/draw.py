import pygame
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 15) # Red
    object_list.append(ball)

    bouncing_ball = BouncingBall(SCREEN_SIZE, Vector2(50, 50), Vector2(9, 9), [0, 255, 0], 15) # Green
    object_list.append(bouncing_ball)

    rainbow_ball = RainbowBall(SCREEN_SIZE, Vector2(400, 300), Vector2(1, 5), [255, 0, 0], 15) # Various
    object_list.append(rainbow_ball)

    bouncing_rainbow_ball = BouncingRainbow(SCREEN_SIZE, Vector2(300, 150), Vector2(-4, 0), [0, 255, 0], 8)
    object_list.append(bouncing_rainbow_ball)

    # TODO: Create other ball types for testing

    # Kinetic Balls
    # Red Balls
    for i in range(0, 2):
        kinetic = KineticBall(1, object_list, SCREEN_SIZE,
                                        Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                        Vector2(4*random.random() - 2, 4*random.random() - 2),
                                        [255, 10, 0], 20)
        object_list.append(kinetic)

    # Green Balls
    for i in range(0, 10):
        kinetic = KineticBouncing(1, object_list, SCREEN_SIZE,
                                        Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                        Vector2(4*random.random() - 2, 4*random.random() - 2),
                                        [10, 255, 0], 20)
        object_list.append(kinetic)

    # Various Colors
    for i in range(0, 10):
        kinetic = AllTheThings(1, object_list, SCREEN_SIZE,
                                        Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                        Vector2(4*random.random() - 2, 4*random.random() - 2),
                                        [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)],
                                        random.randint(3, 20))
        object_list.append(kinetic)    
    
def debug_create_blocks(object_list):
    block = Block(SCREEN_SIZE, Vector2(100, 100), 20, 20, [0, 255, 0])
    object_list.extend((block, ))

    block = RainbowBlock(SCREEN_SIZE, Vector2(150, 100), 60, 30, [255, 255, 0])
    object_list.extend((block, ))

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = [] # list of objects of all types in the toy

    debug_create_objects(object_list)
    debug_create_blocks(object_list)

    while True: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
                # pygame.quit()
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
