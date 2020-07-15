import pygame
import sys
import random
import enum


width = 10
height = 10
cell_size = 50

already_been = []
path = []
current_pos = (0, 0)


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


def step_back():
    global current_pos
    if len(path) == 1:
        print("finished labyrinth!")
        pygame.time.wait(10000)
        quit()

    path.pop()
    current_pos = path[len(path)-1]

pygame.init()
screen = pygame.display.set_mode([width*cell_size, height*cell_size])


already_been.append(current_pos)
path.append(current_pos)

pygame.draw.rect(screen, (0, 0, 255), (current_pos[0] * cell_size, current_pos[1] * cell_size, cell_size, cell_size))
pygame.display.update()


while 1:
    next_possibles = get_possible_dir(current_pos[0], current_pos[1])

    if len(next_possibles) == 0:
        step_back()
    else:
        index__ = random.randint(0, len(next_possibles)-1)
        next_choice = next_possibles[index__]

        point_before = current_pos
        current_pos = next_choice

        already_been.append(current_pos)
        path.append(current_pos)

        if point_before[0] != current_pos[0]:
            pygame.draw.rect(screen, (0, 0, 0), (current_pos[0] * cell_size, current_pos[1] * cell_size - 2, cell_size, 4))
            pygame.draw.rect(screen, (0, 0, 0), (current_pos[0] * cell_size, current_pos[1] * cell_size - 2 +cell_size, cell_size, 4))

            if point_before[0] < current_pos[0]:
                pygame.draw.rect(screen, (0, 0, 0), (current_pos[0] * cell_size - 2 + cell_size, current_pos[1] * cell_size, 4, cell_size))
            else:
                pygame.draw.rect(screen, (0, 0, 0),(current_pos[0] * cell_size - 2, current_pos[1] * cell_size, 4, cell_size))

        else:
            pygame.draw.rect(screen, (0, 0, 0), (current_pos[0] * cell_size-2, current_pos[1] * cell_size, 4, cell_size))
            pygame.draw.rect(screen, (0, 0, 0), (current_pos[0] * cell_size-2 + cell_size, current_pos[1] * cell_size, 4, cell_size))

            if point_before[1] < current_pos[1]:
                pygame.draw.rect(screen, (0, 0, 0), (current_pos[0] * cell_size, current_pos[1] * cell_size - 2 + cell_size, cell_size, 4))
            else:
                pygame.draw.rect(screen, (0, 0, 0),(current_pos[0] * cell_size, current_pos[1] * cell_size - 2, cell_size, 4))


        pygame.draw.rect(screen, (0, 0, 255), (current_pos[0] * cell_size, current_pos[1] * cell_size, cell_size, cell_size))
        pygame.display.update()
        pygame.time.wait(100)
