import pygame
import sys
from init import *
from functions import *


direction ="RIGHT"
clock = pygame.time.Clock()
food = generate_food(snake)
alive = True


while True:
    game_display.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"


    snake, food, alive = update(snake, food, direction, alive)
    
    if not alive:
        direction = ""
        if DELAY == 0:
            DELAY = 10
            snake, food, direction, alive = restart()
        else:
            DELAY -= 1

    show(game_display, snake, food)
    pygame.display.update()
    clock.tick(SPEED)