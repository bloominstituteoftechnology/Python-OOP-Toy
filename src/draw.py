import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from rect import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list, paddle_list, enemies_list):
    for i in range(1):
        ball = RainbowBall(SCREEN_SIZE, Vector2(random.randint(100, 400),
                                        random.randint(100, 400)),
                                        Vector2(random.random(), 5),
                                        [255, 0, 0], 10)
        object_list.append(ball)

    paddle = Paddle(SCREEN_SIZE, [300, 450, 50, 10], [0, 0, 0])
    paddle_list.append(paddle)

    for i in range(5):
        color = [random.randint(100, 250), random.randint(100, 250), random.randint(100, 250)]
        for j in range(3):
            enemy = Enemy(SCREEN_SIZE, [ (180 + (55 * i)) , (50 + (20 * j)) , 50, 10 ], color)
            enemies_list.append(enemy)
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    paddle_list = []
    enemies_list = []

    debug_create_objects(object_list, paddle_list, enemies_list)

    while len(enemies_list) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # Logic Loop TODO: Move paddle
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print(1)

        for ball in object_list:
            ball.update()
 
        # Draw Loop
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)
        for paddle in paddle_list:
            paddle.draw(screen, pygame)
        for enemy in enemies_list:
            enemy.draw(screen, pygame)
 
        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
