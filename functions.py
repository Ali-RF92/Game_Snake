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
        if snake[-1][0]+1 > (WIN_SIZE[1]//TILE_SIZE) - 1:
            snake.append([0, snake[-1][1]])
        else:
            snake.append([snake[-1][0] + 1, snake[-1][1]])

    elif direction == "LEFT":
        if snake[-1][0]-1 < 0:
            snake.append([(WIN_SIZE[1]//TILE_SIZE) - 1, snake[-1][1]])
        else:
            snake.append([snake[-1][0] - 1 , snake[-1][1]])

    elif direction == "UP":
        if snake[-1][1]-1 < 0:
            snake.append([snake[-1][0], (WIN_SIZE[0]//TILE_SIZE) - 1])  
        else:
            snake.append([snake[-1][0], snake[-1][1] - 1])

    elif direction == "DOWN":
        if snake[-1][1]+1 > (WIN_SIZE[1]//TILE_SIZE) - 1:
            snake.append([snake[-1][0], 0])
        else:
            snake.append([snake[-1][0], snake[-1][1]+1])

    return snake
