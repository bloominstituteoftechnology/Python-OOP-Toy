import pygame  # TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]
GRAVITY_ACCELERATION = 0.15


def debug_create_balls(object_list):
    # ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    # object_list.append(ball)
    # TODO: Create other ball types for testing
    ball = KineticBall(SCREEN_SIZE, Vector2(50, 50),
                       Vector2(3, -5), [0, 255, 0], 30)
    object_list.append(ball)
    ball = KineticBall(SCREEN_SIZE, Vector2(150, 50),
                       Vector2(3, -5), [0, 255, 0], 30)
    object_list.append(ball)
    ball = KineticBall(SCREEN_SIZE, Vector2(250, 50),
                       Vector2(3, -5), [0, 255, 0], 30)
    object_list.append(ball)
    ball = KineticBall(SCREEN_SIZE, Vector2(550, 50),
                       Vector2(-3, 3), [255, 0, 0], 30)
    object_list.append(ball)
    ball = KineticBall(SCREEN_SIZE, Vector2(550, 450),
                       Vector2(-3, 5), [255, 0, 0], 20)
    object_list.append(ball)
    ball = KineticBall(SCREEN_SIZE, Vector2(350, 350),
                       Vector2(-3, 5), [255, 0, 0], 20)
    object_list.append(ball)

    # ball = BouncingBall(SCREEN_SIZE, Vector2(50, 40), Vector2(
    #     3, 0), [0, 250, 0], 10, GRAVITY_ACCELERATION)
    # object_list.append(ball)
    # ball = RainbowBall(SCREEN_SIZE, Vector2(50, 70),
    #                    Vector2(3, 1), [0, 0, 250], 10)
    # object_list.append(ball)
    # ball = BouncingRainbow(SCREEN_SIZE, Vector2(50, 70), Vector2(
    #     3, -4), [0, 250, 0], 20, GRAVITY_ACCELERATION)
    # object_list.append(ball)


def debug_create_blocks(object_list):
    block = Block(SCREEN_SIZE, Vector2(100, 100), 20, 20, [0, 255, 0])
    object_list.extend((block, ))


def debug_start_game(object_list):
    debug_create_balls(object_list)
    debug_create_blocks(object_list)


def slopes(currentObjPosition, nextObjectPosition):
    print(currentObjPosition, nextObjectPosition)
    objX = currentObjPosition.x
    objY = currentObjPosition.y
    itemX = nextObjectPosition.x
    itemY = nextObjectPosition.y
    if (objX - itemX) == 0:
        slope = 0
    else:
        slope = (objY - itemY) / (objX - itemX)
    return slope


def detectCollision(obj, colliding_objs):
    '''
    If there are collision return true.
    obj: is the current item in the for loop inside main().
    colliding_objs: List of objects that can collide.
    '''
    collision = False
    print('detectColision')
    for i in range(len(colliding_objs)):
        # print(obj == item)
        item = colliding_objs[i]
        print(obj)
        print(item)
        print(len(colliding_objs), colliding_objs)
        if not obj == item:  # If obj is not itself
            print(obj == item)

            # Here we detecto collision base on 'next' state/frame
            # if in the 'next' state/frmae the balls collide so we take actions.
            # if not: 'updeate' the ball as usual
            obj_radius = obj.radius
            item_radius = item.radius
            sumOfRadius = obj_radius + item_radius

            currentObjPosition = obj.position
            nextObjPosition = obj.position + obj.velocity

            itemCurrentPosition = item.position
            nextItemPosition = item.position + item.velocity

            nextDistance = nextObjPosition.distance_to(nextItemPosition)

            if nextDistance < sumOfRadius:
                objSelfTrayectorySlope = slopes(
                    currentObjPosition, nextObjPosition)
                itemSelfTrayectorySlope = slopes(
                    itemCurrentPosition, nextItemPosition)
                nextSlopeBetweenBalls = slopes(
                    nextObjPosition, nextItemPosition)

                collision = True

            elif nextDistance == sumOfRadius:
                collision = True
                pass

    return collision


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
                    Kinetic_List = []
                    for obj in object_list:
                        if isinstance(obj, KineticBall):
                            print(obj)
                            Kinetic_List.append(obj)
                if event.key == pygame.K_q:
                    pygame.quit()

        # print('Kinetic_List', len(Kinetic_List))
        for obj in object_list:
            # Detect collision -> if collision set new variables in Objs
            if isinstance(obj, KineticBall):
                print('isinstance')
                if detectCollision(obj, Kinetic_List):
                    obj.collide(0, 0)
                    pass
                else:
                    obj.update()
            else:
                # Paint new state
                obj.update()
        print('END')
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
