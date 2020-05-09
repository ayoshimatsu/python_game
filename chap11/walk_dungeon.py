import pygame
import sys
import random

BLACK = (0, 0, 0)

LABY_WIDTH = 11
LABY_HEIGHT = 9
laby = []
for y in range(LABY_HEIGHT):
    laby.append([0] * LABY_WIDTH)

DUNGEON_WIDTH = LABY_WIDTH * 3
DUNGEON_HEIGHT = LABY_HEIGHT * 3
dungeon = []
for y in range(DUNGEON_HEIGHT):
    dungeon.append([0] * DUNGEON_WIDTH)

imgWall = pygame.image.load("images/wall.png")
imgFloor = pygame.image.load("images/floor.png")
imgPlayer = pygame.image.load("images/player.png")

pl_x = 4
pl_y = 4

def make_dungeon():
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

    for y in range(DUNGEON_HEIGHT):
        for x in range(DUNGEON_WIDTH):
            dungeon[y][x] = 9

    for y in range(1, LABY_HEIGHT - 1):
        for x in range(1, LABY_WIDTH - 1):
            dx = x * 3 + 1
            dy = y * 3 + 1
            if laby[y][x] == 0:
                if random.randint(0, 99) < 20:
                    for ry in range(-1, 2):
                        for rx in range(-1, 2):
                            dungeon[dy+ry][dx+rx] = 0
                else:
                    dungeon[dy][dx] = 0
                    if laby[y-1][x] == 0:
                        dungeon[dy-1][dx] = 0
                    if laby[y+1][x] == 0:
                        dungeon[dy+1][dx] = 0
                    if laby[y][x-1] == 0:
                        dungeon[dy][dx-1] = 0
                    if laby[y][x+1] == 0:
                        dungeon[dy][dx+1] = 0

def draw_dungeon(bg):
    bg.fill(BLACK)
    for y in range(-5, 6):
        for x in range(-5, 6):
            X = (x+5) * 16
            Y = (y+5) * 16
            dx = pl_x + x
            dy = pl_y + y
            if 0 <= dx and dx < DUNGEON_WIDTH and 0 <= dy and dy < DUNGEON_HEIGHT:
                if dungeon[dy][dx] == 0:
                    bg.blit(imgFloor, [X, Y])
                if dungeon[dy][dx] == 9:
                    bg.blit(imgWall, [X, Y])
            if x == 0 and y == 0:
                bg.blit(imgPlayer, [X, Y-8])

def move_player():
    global pl_x, pl_y
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == 1:
        if dungeon[pl_y-1][pl_x] != 9: pl_y -= 1
    if key[pygame.K_DOWN] == 1:
        if dungeon[pl_y+1][pl_x] != 9: pl_y += 1
    if key[pygame.K_LEFT] == 1:
        if dungeon[pl_y][pl_x-1] != 9: pl_x -= 1
    if key[pygame.K_RIGHT] == 1:
        if dungeon[pl_y][pl_x+1] != 9: pl_x += 1

def main():
    pygame.init()
    pygame.display.set_caption("Create Dungeon")
    screen = pygame.display.set_mode((176, 176))
    clock = pygame.time.Clock()
    make_dungeon()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        move_player()
        draw_dungeon(screen)
        pygame.display.update()
        clock.tick(5)

if __name__ == "__main__":
    main()