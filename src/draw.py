import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from rectangle import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    # ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    ball_count = 5
    # for i in range(ball_count):
    #     ball = BouncingRainbow(SCREEN_SIZE, Vector2(random.randint(100, 400), random.randint(100, 400)),
    #                                      Vector2(random.randint(0, 5), random.randint(0, 5)), [255, 0, 0], 10)
    #     object_list.append(ball)
    # rect1 = Rectangle(SCREEN_SIZE, [255, 0, 0], [175, 10, 150, 100], 2)
    # rect2 = Rectangle(SCREEN_SIZE, [0, 0, 255], [300, 200, 75, 125], 2)
    # object_list.append(rect1)
    # object_list.append(rect2)
    

    # TODO: Create other ball types for testing
    for i in range(ball_count):
        pos = Vector2(random.randint(100, 400), random.randint(100, 400))
        vel = Vector2(random.randint(0, 5), random.randint(0, 5))
        color = [255, 0, 0]
        #radius = 10
        radius = random.randint(10, 40)
        #mass = 1
        mass = random.randint(1, 5)
        # ball = BouncingRainbow(SCREEN_SIZE, pos, vel, color, radius)
        ball = AllTheThings(SCREEN_SIZE, pos, vel, color, radius, mass, object_list)

        object_list.append(ball)
       
  
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
