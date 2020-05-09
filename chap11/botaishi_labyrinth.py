import pygame
import sys
import random

CYAN = (0, 255, 255)
GRAY = (96, 96, 96)

LABY_WIDTH = 11
LABY_HEIGHT = 9
laby = []

for y in range(LABY_HEIGHT):
    laby.append([0] * LABY_WIDTH)

def make_labyrinth():
    XP = [0, 1, 0, -1]
    YP = [-1, 0, 1, 0]

    for x in range(LABY_WIDTH):
        laby[0][x] = 1
        laby[LABY_HEIGHT - 1][x] = 1
    for y in range(LABY_HEIGHT):
        laby[y][0] = 1
        laby[y][LABY_WIDTH - 1] = 1

    for y in range(1, LABY_HEIGHT - 1):
        for x in range(1, LABY_WIDTH - 1):
            laby[y][x] = 0

    for y in range(2, LABY_HEIGHT - 2, 2):
        for x in range(2, LABY_WIDTH - 2, 2):
            laby[y][x] = 1

    for y in range(2, LABY_HEIGHT - 2, 2):
        for x in range(2, LABY_WIDTH - 2, 2):
            d = 0
            if x > 2:
                d = random.randint(0, 2)
            else:
                d = random.randint(0, 3)
            laby[y + YP[d]][x + XP[d]] = 1


def main():
    pygame.init()
    pygame.display.set_caption("Create Labyrinth")
    screen = pygame.display.set_mode((528, 432))
    clock = pygame.time.Clock()
    make_labyrinth()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    make_labyrinth()

        for y in range(LABY_HEIGHT):
            for x in range(LABY_WIDTH):
                W = 48
                H = 48
                X = x * W
                Y = y * H
                if laby[y][x] == 0:
                    pygame.draw.rect(screen, CYAN, [X, Y, W, H])
                if laby[y][x] == 1:
                    pygame.draw.rect(screen, GRAY, [X, Y, W, H])

        pygame.display.update()
        clock.tick(2)

if __name__ == "__main__":
    main()