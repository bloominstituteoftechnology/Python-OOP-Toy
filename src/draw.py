import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    for i in range(5):
        ball = BouncingRainbow(SCREEN_SIZE, Vector2(random.randint(100,400),
                                                    random.randint(100, 400)),
                                                    Vector2(3, 0), [0, 0, 0], 10)
        object_list.append(ball)

    # TODO: Create other ball types for testing
  
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

        #monitor collisions and update
        for ball1 in object_list:
            for ball2 in object_list:
                dist = math.sqrt((ball1.position[0] - ball2.position[0])**2 + (ball1.position[1] - ball2.position[1])**2)
                if dist <= ball1.radius + ball2.radius:
                    ball1.velocity.x *= -1
                    ball1.velocity.y *= -1
                    ball2.velocity.x *= -1
                    ball2.velocity.y *= -1
            ball1.update()

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
