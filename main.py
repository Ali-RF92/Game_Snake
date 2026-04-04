import pygame
import sys
from init import *
from functions import *


direction ="RIGHT"
clock = pygame.time.Clock()

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


    snake = update(snake, direction)
    show(game_display, snake)
    pygame.display.update()
    clock.tick(SPEED)