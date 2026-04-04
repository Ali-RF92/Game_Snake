import pygame
from constants import *
from random import randint as rnd



def show(surface, snake, food):
    for sq in snake:
        pygame.draw.rect(surface, 
                         (255, 255, 255), 
                         (sq[0]*TILE_SIZE, sq[1]*TILE_SIZE,
                           TILE_SIZE, 
                           TILE_SIZE),
                           1
                           )
        pygame.draw.rect(surface,
                         (255, 0, 0),
                         (food[0]*TILE_SIZE, food[1]*TILE_SIZE,
                           TILE_SIZE, 
                           TILE_SIZE),
                           )

def update(snake, food, direction, alive):

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

    if food not in snake:
        snake.pop(0)
    else:
        food = generate_food(snake)

    if snake[-1] in snake[:-1]:
        alive = False
    return snake, food, alive



def generate_food(snake):
    food = [rnd(0, (WIN_SIZE[0]//TILE_SIZE) - 1), rnd(0, (WIN_SIZE[1]//TILE_SIZE) - 1)]
    while food in snake:
        food = [rnd(0, (WIN_SIZE[0]//TILE_SIZE) - 1), rnd(0, (WIN_SIZE[1]//TILE_SIZE) - 1)]
    return food