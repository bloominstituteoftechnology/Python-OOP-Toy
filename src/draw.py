import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]
GRAVITY_ACCELERATION = 0.15


def debug_create_balls(object_list):
    ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    object_list.append(ball)
    # TODO: Create other ball types for testing
    ball = KineticBall(SCREEN_SIZE, Vector2(50, 50),
                       Vector2(3, -5), [0, 255, 0], 30)
    object_list.append(ball)
    ball = KineticBall(SCREEN_SIZE, Vector2(550, 50),
                       Vector2(-3, 3), [255, 0, 0], 30)
    object_list.append(ball)

    ball = BouncingBall(SCREEN_SIZE, Vector2(50, 40), Vector2(
        3, 0), [0, 250, 0], 10, GRAVITY_ACCELERATION)
    object_list.append(ball)
    ball = RainbowBall(SCREEN_SIZE, Vector2(50, 70),
                       Vector2(3, 1), [0, 0, 250], 10)
    object_list.append(ball)
    ball = BouncingRainbow(SCREEN_SIZE, Vector2(50, 70), Vector2(
        3, -4), [0, 250, 0], 20, GRAVITY_ACCELERATION)
    object_list.append(ball)


def debug_create_blocks(object_list):
    block = Block(SCREEN_SIZE, Vector2(100, 100), 20, 20, [0, 255, 0])
    object_list.extend((block, ))


def debug_start_game(object_list):
    debug_create_balls(object_list)
    debug_create_blocks(object_list)


def slopes(obj, nextObjectPosition):
    objX = obj.position.x
    objY = obj.position.y
    itemX = nextObjectPosition.x
    itemY = nextObjectPosition.y
    if (objX - itemX) == 0:
        slope = 0
    else:
        slope = (objY - itemY) / (objX - itemX)
    return slope


def detectCollision(obj, colliding_objs):
    '''If there are collision return true'''
    for item in colliding_objs:
        if not obj == item:  # If obj is not itself
            obj_radius = obj.radius
            item_radius = item.radius
            sumOfRadius = obj_radius + item_radius
            nextObjPosition = obj.position + obj.velocity
            nextItemPosition = item.position + item.velocity
            distance = nextObjPosition.distance_to(nextItemPosition)

            if distance <= sumOfRadius:
                objSlope = slopes(obj, nextObjPosition)
                itemSlope = slopes(item, nextItemPosition)

                return True

            elif distance == sumOfRadius:
                pass
            else:
                return False


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    object_list = []  # list of objects of all types in the toy
    Kinetic_List = []

    while True:  # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:  # TODO:  Get working
                if event.key == pygame.K_SPACE:
                    # TODO: Add behavior when button pressed
                    print(event)
                if event.key == pygame.K_s:
                    debug_start_game(object_list)
                    for obj in object_list:
                        if isinstance(obj, KineticBall):
                            Kinetic_List.append(obj)
                if event.key == pygame.K_q:
                    pygame.quit()

        print('Kinetic_List', len(Kinetic_List))
        for obj in object_list:
            # Detect collision -> if collision set new variables in Objs
            if isinstance(obj, KineticBall):
                # print('isinstance')
                if detectCollision(obj, Kinetic_List):
                    obj.collide(0, 0)
                    pass
                else:
                    obj.update()
            else:
                # Paint new state
                obj.update()

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
