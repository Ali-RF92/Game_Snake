import pygame
from constants import *




def show(surface, snake):
    for sq in snake:
        pygame.draw.rect(surface, 
                         (255, 255, 255), 
                         (sq[0]*TILE_SIZE, sq[1]*TILE_SIZE,
                           TILE_SIZE, 
                           TILE_SIZE),
                           1
                           )
        
def update(snake, direction):
    snake.pop(0)
    if direction == "RIGHT":
        snake.append([snake[-1][0] + 1, snake[-1][1]])

    elif direction == "LEFT":
        snake.append([snake[-1][0] - 1, snake[-1][1]])
        
    elif direction == "UP":
        snake.append([snake[-1][0], snake[-1][1] - 1])

    elif direction == "DOWN":
        snake.append([snake[-1][0], snake[-1][1]+1])
    

    return snake
