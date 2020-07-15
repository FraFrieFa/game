import pygame
import sys
import random
import enum


width = 10
height = 10
cell_size = 50

already_been = []


def get_possible_dir(x_, y_):
    res = []
    if x_ > 0:
        res.append((x_-1, y_))
    if x_ < width-1:
        res.append((x_+1, y_))
    if y_ > 0:
        res.append((x_, y_-1))
    if y_ < width - 1:
        res.append((x_, y_+1))
    real_res = []
    for sample in res:
        if not already_been.__contains__(sample):
            real_res.append(sample)
    return real_res


pygame.init()
screen = pygame.display.set_mode([600, 600])


current_pos = (0, 0)
already_been.append(current_pos)

pygame.draw.rect(screen, (0, 0, 255), (current_pos[0] * cell_size, current_pos[1] * cell_size, cell_size, cell_size))
pygame.display.update()


while 1:
    next_possibles = get_possible_dir(current_pos[0], current_pos[1])

    if len(next_possibles) == 0:
        break

    index__ = random.randint(0, len(next_possibles)-1)
    next_choice = next_possibles[index__]

    current_pos = next_choice

    already_been.append(current_pos)

    pygame.draw.rect(screen, (0, 0, 255), (current_pos[0] * cell_size, current_pos[1] * cell_size, cell_size, cell_size))
    pygame.display.update()
    pygame.time.wait(200)




