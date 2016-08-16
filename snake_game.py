#!/usr//bin/python
# -*- coding: utf-8 -*-
import random 

x_axis, y_axis = 10, 10

def draw_map(snake, apples):
    # make a empty map with dots
    table = []
    for i in range(x_axis):
        column = []
        for j in range(y_axis):
            column.append('.')
        table.append(column)
    # change dots to X where the snake is
    for X in snake:
        table[X[0]][X[1]] = 'X'
    # change dots to ? where the apples are
    for apple in apples:
        table[apple[0]][apple[1]] = '?'
    # draw a map with snake
    printout = ''
    for j in range(len(table[0])):
        for i in range(len(table)):
            printout += ''.join(table[i][j])
        printout += '\n'
    print printout
    
    
def move(snake, direction, apples, nb):
    if len(snake) > 0:
        directions = {'W':(-1, 0), 'E':(1, 0), 'S':(0, 1), 'N':(0, -1)}
        movement = directions[direction]
        first = (snake[-1][0] + movement[0], snake[-1][1] + movement[1])
        if first in snake:
            raise ValueError('Game over!')
        if (first[0] not in range(x_axis)) or (first[1] not in range(y_axis)):
            raise ValueError('Game over!')
        if first in apples:
            apples.remove(first)
            while True:
                apple = (random.choice(range(x_axis)), 
                         random.choice(range(y_axis))
                         )
                if apple not in apples + snake + [first]:
                    apples.append(apple)
                    break
        else:
            if nb % 10 != 0: del snake[0]
        snake.append(first)
    else:
        raise ValueError('Length of snake is 0!')
        
Help = '''
Use S, W, E and N to indicate the direction of motion.
Don't run the snake into the wall, or his own tail.
Eat the apples to gain points. 
'''      
snake = [(0, 0), (1, 0), (2,0)]
apples = [(4, 5)]
number_of_moves = 1
print Help
while True:
    draw_map(snake, apples)
    direction = raw_input('Which direction?')
    direction = direction.upper()
    if len(direction) > 1 or direction == '':
        print 'I don\'t understand!'
        continue
    if direction == '?':
        print Help
        continue
    if direction not in 'WESN':
        print 'I don\'t understand!'
        print Help
    else:
        move(snake, direction, apples, number_of_moves)
        number_of_moves += 1
        