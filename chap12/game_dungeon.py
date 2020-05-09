import pygame
import sys
import random
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
BLINK = [(224, 255, 255), (192, 240, 255), (128, 224, 255), (64, 192, 255), (128, 224, 255), (192, 240, 255)]

imgTitle = pygame.image.load("image/title.png")
imgWall = pygame.image.load("image/wall.png")
imgWall2 = pygame.image.load("image/wall2.png")
imgDark = pygame.image.load("image/dark.png")
imgPara = pygame.image.load("image/parameter.png")
imgBtlBG = pygame.image.load("image/btlbg.png")
imgEnemy = pygame.image.load("image/enemy0.png")

imgItem = [
    pygame.image.load("image/potion.png"),
    pygame.image.load("image/blaze_gem.png"),
    pygame.image.load("image/spoiled.png"),
    pygame.image.load("image/apple.png"),
    pygame.image.load("image/meat.png")
]
imgFloor = [
    pygame.image.load("image/floor.png"),
    pygame.image.load("image/tbox.png"),
    pygame.image.load("image/cocoon.png"),
    pygame.image.load("image/stairs.png")
]
imgPlayer = [
    pygame.image.load("image/mychr0.png"),
    pygame.image.load("image/mychr1.png"),
    pygame.image.load("image/mychr2.png"),
    pygame.image.load("image/mychr3.png"),
    pygame.image.load("image/mychr4.png"),
    pygame.image.load("image/mychr5.png"),
    pygame.image.load("image/mychr6.png"),
    pygame.image.load("image/mychr7.png"),
    pygame.image.load("image/mychr8.png")
]
imgEffect = [
    pygame.image.load("image/effect_a.png"),
    pygame.image.load("image/effect_b.png")
]

speed = 1
idx = 0
tmr = 0
floor = 0
fl_max = 1
welcome = 0

pl_x = 0
pl_y = 0
pl_d = 0
pl_a = 0
pl_lifemax = 0
pl_life = 0
pl_str = 0
food = 0
potion = 0
blazegem = 0
treasure = 0

emy_name = ""
emy_lifemax = 0
emy_life = 0
emy_str = 0
emy_x = 0
emy_y = 0
emy_step = 0
emy_blink = 0

dmg_eff = 0
btl_cmd = 0

COMMAND = ["[A]ttack", "[P]otion", "[B]laze gem", "[R]un"]
TRE_NAME = ["Potion", "Blaze gem", "Food spoiled.", "Food +20", "Food +100"]
EMY_NAME = ["Green slime", "Red slime", "Axe beast", "Ogre", "Sword man",
            "Death hornet", "Signal slime", "Devil plant", "Twin killer", "Hell"]

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
                    if laby[y-1][x] == 0: dungeon[dy-1][dx] = 0
                    if laby[y+1][x] == 0: dungeon[dy+1][dx] = 0
                    if laby[y][x-1] == 0: dungeon[dy][dx-1] = 0
                    if laby[y][x+1] == 0: dungeon[dy][dx+1] = 0

def draw_dungeon(bg, fnt):
    bg.fill(BLACK)
    for y in range(-4, 6):
        for x in range(-5, 6):
            X = (x + 5) * 80
            Y = (y + 4) * 80
            dx = pl_x + x
            dy = pl_y + y
            if 0 <= dx and dx < DUNGEON_WIDTH and 0 <= dy and dy < DUNGEON_HEIGHT:
                if dungeon[dy][dx] <= 3:
                    bg.blit(imgFloor[dungeon[dy][dx]], [X, Y])
                if dungeon[dy][dx] == 9:
                    bg.blit(imgWall, [X, Y-40])
                    if dy >= 1 and dungeon[dy-1][dx] == 9:
                        bg.blit(imgWall2, [X, Y-80])
            if x == 0 and y == 0:
                bg.blit(imgPlayer[pl_a], [X, Y-40])
    bg.blit(imgDark, [0, 0])
    draw_para(bg, fnt)

def put_event():    #Assign Event on Floor
    global pl_x, pl_y, pl_a, pl_d

    while True: # Set stairs
        x = random.randint(3, DUNGEON_WIDTH - 4)
        y = random.randint(3, DUNGEON_HEIGHT - 4)
        if dungeon[y][x] == 0:
            for ry in range(-1, 2):
                for rx in range(-1, 2):
                    dungeon[y+ry][x+rx] = 0
            dungeon[y][x] = 3
            break

    for i in range(60): #Set Treasure and Cocoon
        x = random.randint(3, DUNGEON_WIDTH - 4)
        y = random.randint(3, DUNGEON_HEIGHT - 4)
        if dungeon[y][x] == 0:
            dungeon[y][x] = random.choice([1, 2, 2, 2, 2])

    while True: #Initial position of player
        pl_x = random.randint(3, DUNGEON_WIDTH - 4)
        pl_y = random.randint(3, DUNGEON_HEIGHT - 4)
        if dungeon[pl_y][pl_x] == 0:
            break
    pl_d = 1
    pl_a = 2

def move_player(key):
    global idx, tmr, pl_x, pl_y, pl_d, pl_a, pl_life, food, potion, blazegem, treasure

    if dungeon[pl_y][pl_x] == 1:  # 宝箱に載った
        dungeon[pl_y][pl_x] = 0
        treasure = random.choice([0, 0, 0, 1, 1, 1, 1, 1, 1, 2])
        if treasure == 0:
            potion = potion + 1
        if treasure == 1:
            blazegem = blazegem + 1
        if treasure == 2:
            food = int(food / 2)
        idx = 3
        tmr = 0
        return
    if dungeon[pl_y][pl_x] == 2:  # 繭に載った
        dungeon[pl_y][pl_x] = 0
        r = random.randint(0, 99)
        if r < 40:  # 食料
            treasure = random.choice([3, 3, 3, 4])
            if treasure == 3: food = food + 20
            if treasure == 4: food = food + 100
            idx = 3
            tmr = 0
        else:  # 敵出現
            idx = 10
            tmr = 0
        return
    if dungeon[pl_y][pl_x] == 3:  # 階段に載った
        idx = 2
        tmr = 0
        return

    x = pl_x
    y = pl_y
    if key[K_UP] == 1:
        pl_d = 0
        if dungeon[pl_y - 1][pl_x] != 9: pl_y -= 1
    if key[K_DOWN] == 1:
        pl_d = 1
        if dungeon[pl_y + 1][pl_x] != 9: pl_y += 1
    if key[K_LEFT] == 1:
        pl_d = 2
        if dungeon[pl_y][pl_x - 1] != 9: pl_x -= 1
    if key[K_RIGHT] == 1:
        pl_d = 3
        if dungeon[pl_y][pl_x + 1] != 9: pl_x += 1
    pl_a = pl_d * 2
    if pl_x != x or pl_y != y:
        pl_a += tmr % 2
        if food > 0:
            food -= 1
            if pl_life < pl_lifemax:
                pl_life += 1
        else:
            pl_life -= 5
            if pl_life <= 0:
                pl_life = 0
                #pygame.mixer.music.stop()
                idx = 9
                tmr = 0

def draw_text(bg, txt, x, y, fnt, col):
    sur = fnt.render(txt, True, BLACK)
    bg.blit(sur, [x+1, y+2])
    sur = fnt.render(txt, True, col)
    bg.blit(sur, [x, y])

def draw_para(bg, fnt):
    X = 30
    Y = 600
    bg.blit(imgPara, [X, Y])
    col = WHITE
    if pl_life < 10 and tmr % 2 == 0: col = RED
    draw_text(bg, "{}/{}".format(pl_life, pl_lifemax), X+128, Y+6, fnt, col)
    draw_text(bg, str(pl_str), X+128, Y+33, fnt, WHITE)
    col = WHITE
    if food == 0 and tmr % 2 == 0: col = RED
    draw_text(bg, str(food), X + 128, Y + 60, fnt, col)
    draw_text(bg, str(potion), X + 266, Y + 6, fnt, WHITE)
    draw_text(bg, str(blazegem), X + 266, Y + 33, fnt, WHITE)

def init_battle():
    global imgEnemy, emy_name, emy_lifemax, emy_life, emy_str, emy_x, emy_y
    typ = random.randint(0, floor)
    if floor >= 10:
        typ = random.randint(0, 9)
    lev = random.randint(1, floor)
    imgEnemy = pygame.image.load("image/enemy" + str(typ) + ".png")
    emy_name = EMY_NAME[typ] + "LV" + str(lev)
    emy_lifemax = 60 * (typ + 1) + (lev - 1) * 10
    emy_life = emy_lifemax
    emy_str = int(emy_lifemax / 8)
    emy_x = 440 - imgEnemy.get_width() / 2
    emy_y = 560 - imgEnemy.get_height()

def draw_bar(bg, x, y, w, h, val, max): #HP bar of Enemy
    pygame.draw.rect(bg, WHITE, [x-2, y-2, w+4, h+4])
    pygame.draw.rect(bg, BLACK, [x, y, w, h])
    if val > 0:
        pygame.draw.rect(bg, (0,128,255), [x, y, w*val/max, h])

def draw_battle(bg, fnt):   #Display Screen of Battle
    global emy_blink, dmg_eff
    bx = 0
    by = 0
    if dmg_eff > 0:
        dmg_eff -= 1
        bx = random.randint(-20, 20)
        by = random.randint(-10, 10)
    bg.blit(imgBtlBG, [bx, by])
    if emy_life and emy_blink % 2 == 0:
        bg.blit(imgEnemy, [emy_x, emy_y + emy_step])
    draw_bar(bg, 340, 580, 200, 10, emy_life, emy_lifemax)
    if emy_blink > 0:
        emy_blink -= 1
    for i in range(10):
        draw_text(bg, message[i], 600, 100 + i * 50, fnt, WHITE)
    draw_para(bg, fnt)

def battle_command(bg, fnt, key):   #Input and display Command
    global btl_cmd
    ent = False
    if key[K_a]:  # Aキー
        btl_cmd = 0
        ent = True
    if key[K_p]:  # Pキー
        btl_cmd = 1
        ent = True
    if key[K_b]:  # Bキー
        btl_cmd = 2
        ent = True
    if key[K_r]:  # Rキー
        btl_cmd = 3
        ent = True
    if key[K_UP] and btl_cmd > 0:  # ↑キー
        btl_cmd -= 1
    if key[K_DOWN] and btl_cmd < 3:  # ↓キー
        btl_cmd += 1
    if key[K_SPACE] or key[K_RETURN]:
        ent = True
    for i in range(4):
        c = WHITE
        if btl_cmd == i: c = BLINK[tmr % 6]
        draw_text(bg, COMMAND[i], 20, 360 + i * 60, fnt, c)
    return ent

message = [""] * 10
def init_message():
    for i in range(10):
        message[i] = ""

def set_message(msg):
    for i in range(10):
        if message[i] == "":
            message[i] = msg
            return
    for i in range(9):
        message[i] = message[i + 1]
    message[9] = msg

def main():
    global speed, idx, tmr, floor, fl_max, welcome
    global pl_a, pl_lifemax, pl_life, pl_str, food, potion, blazegem
    global emy_life, emy_step, emy_blink, dmg_eff
    dmg = 0
    lif_p = 0
    str_p = 0

    pygame.init()
    pygame.display.set_caption("One hour Dungeon")
    screen = pygame.display.set_mode((880, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)
    fontS = pygame.font.Font(None, 30)

    """
    se = [ # 効果音とジングル
        pygame.mixer.Sound("sound/ohd_se_attack.ogg"),
        pygame.mixer.Sound("sound/ohd_se_blaze.ogg"),
        pygame.mixer.Sound("sound/ohd_se_potion.ogg"),
        pygame.mixer.Sound("sound/ohd_jin_gameover.ogg"),
        pygame.mixer.Sound("sound/ohd_jin_levup.ogg"),
        pygame.mixer.Sound("sound/ohd_jin_win.ogg")
    ]
    """

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    speed = speed + 1
                    if speed == 4:
                        speed = 1

        tmr = tmr + 1
        key = pygame.key.get_pressed()

        if idx == 0:  # Title Screen
            #if tmr == 1:
                #pygame.mixer.music.load("sound/ohd_bgm_title.ogg")
                #pygame.mixer.music.play(-1)
            screen.fill(BLACK)
            screen.blit(imgTitle, [40, 60])
            if fl_max >= 2:
                draw_text(screen, "You reached floor {}.".format(fl_max), 300, 460, font, CYAN)
            draw_text(screen, "Press space key", 320, 560, font, BLINK[tmr % 6])
            if key[K_SPACE] == 1:
                make_dungeon()
                put_event()
                floor = 1
                welcome = 15
                pl_lifemax = 300
                pl_life = pl_lifemax
                pl_str = 100
                food = 300
                potion = 0
                blazegem = 0
                idx = 1
                #pygame.mixer.music.load("sound/ohd_bgm_field.ogg")
                #pygame.mixer.music.play(-1)

        elif idx == 1:  #Move Player
            move_player(key)
            draw_dungeon(screen, fontS)
            draw_text(screen, "floor {} ({},{})".format(floor, pl_x, pl_y), 60, 40, fontS, WHITE)
            if welcome > 0:
                welcome = welcome - 1
                draw_text(screen, "Welcome to floor {}.".format(floor), 300, 180, font, CYAN)

        elif idx == 2:  #Switch Screen
            draw_dungeon(screen, fontS)
            if 1 <= tmr and tmr <= 5:
                h = 80 * tmr
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
                pygame.draw.rect(screen, BLACK, [0, 720 - h, 880, h])
            if tmr == 5:
                floor = floor + 1
                if floor > fl_max:
                    fl_max = floor
                welcome = 15
                make_dungeon()
                put_event()
            if 6 <= tmr and tmr <= 9:
                h = 80 * (10 - tmr)
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h])
                pygame.draw.rect(screen, BLACK, [0, 720 - h, 880, h])
            if tmr == 10:
                idx = 1

        elif idx == 3:  #Get an item or Fall into a trap
            draw_dungeon(screen, fontS)
            screen.blit(imgItem[treasure], [320, 220])
            draw_text(screen, TRE_NAME[treasure], 380, 240, font, WHITE)
            if tmr == 10:
                idx = 1

        elif idx == 9:  #Gameover
            if tmr <= 30:
                PL_TURN = [2, 4, 0, 6]
                pl_a = PL_TURN[tmr % 4]
                if tmr == 30: pl_a = 8  #Picture of fallen player
                draw_dungeon(screen, fontS)
            elif tmr == 31:
                #se[3].play()
                draw_text(screen, "You died.", 360, 240, font, RED)
                draw_text(screen, "Game over.", 360, 380, font, RED)
            elif tmr == 100:
                idx = 0
                tmr = 0

        elif idx == 10: #Battle start
            if tmr == 1:
                #pygame.mixer.music.load("sound/ohd_bgm_battle.ogg")
                #pygame.mixer.music.play(-1)
                init_battle()
                init_message()
            elif tmr <= 4:
                bx = (4 - tmr) * 220
                by = 0
                screen.blit(imgBtlBG, [bx, by])
                draw_text(screen, "Encounter!", 350, 200, font, WHITE)
            elif tmr <= 16:
                draw_battle(screen, fontS)
                draw_text(screen, emy_name + " appear!", 300, 200, font, WHITE)
            else:
                idx = 11
                tmr = 0

        elif idx == 11:  #Turn of Player(Wait for Input)
            draw_battle(screen, fontS)
            if tmr == 1: set_message("Your turn.")
            if battle_command(screen, font, key) == True:
                if btl_cmd == 0:
                    idx = 12
                    tmr = 0
                if btl_cmd == 1 and potion > 0:
                    idx = 20
                    tmr = 0
                if btl_cmd == 2 and blazegem > 0:
                    idx = 21
                    tmr = 0
                if btl_cmd == 3:
                    idx = 14
                    tmr = 0

        elif idx == 12:     #Player Attack
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("You attack!")
                #se[0].play()
                dmg = pl_str + random.randint(0, 9)
            if 2 <= tmr and tmr <= 4:
                screen.blit(imgEffect[0], [700 - tmr * 120, -100 + tmr * 120])
            if tmr == 5:
                emy_blink = 5
                set_message(str(dmg) + "pts of damage!")
            if tmr == 11:
                emy_life = emy_life - dmg
                if emy_life <= 0:
                    emy_life = 0
                    idx = 16
                    tmr = 0
            if tmr == 16:
                idx = 13
                tmr = 0

        elif idx == 13:  #Turn of Enemy, Enemy Attack
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("Enemy turn.")
            if tmr == 5:
                set_message(emy_name + " attack!")
                #se[0].play()
                emy_step = 30
            if tmr == 9:
                dmg = emy_str + random.randint(0, 9)
                set_message(str(dmg) + "pts of damage!")
                dmg_eff = 5
                emy_step = 0
            if tmr == 15:
                pl_life = pl_life - dmg
                if pl_life < 0:
                    pl_life = 0
                    idx = 15
                    tmr = 0
            if tmr == 20:
                idx = 11
                tmr = 0

        elif idx == 14:  #Run Away?
            draw_battle(screen, fontS)
            if tmr == 1: set_message("...")
            if tmr == 2: set_message("......")
            if tmr == 3: set_message(".........")
            if tmr == 4: set_message("............")
            if tmr == 5:
                if random.randint(0, 99) < 60:
                    idx = 22
                else:
                    set_message("You failed to flee.")
            if tmr == 10:
                idx = 13
                tmr = 0

        elif idx == 15:  # Lose
            draw_battle(screen, fontS)
            if tmr == 1:
                #pygame.mixer.music.stop()
                set_message("You lose.")
            if tmr == 11:
                idx = 9
                tmr = 29

        elif idx == 16:  # Victory
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("You win!")
                #pygame.mixer.music.stop()
                #se[5].play()
            if tmr == 28:
                idx = 22
                if random.randint(0, emy_lifemax) > random.randint(0, pl_lifemax):
                    idx = 17
                    tmr = 0

        elif idx == 17:  # レベルアップ
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("Level up!")
                #se[4].play()
                lif_p = random.randint(10, 20)
                str_p = random.randint(5, 10)
            if tmr == 21:
                set_message("Max life + " + str(lif_p))
                pl_lifemax = pl_lifemax + lif_p
            if tmr == 26:
                set_message("Str + " + str(str_p))
                pl_str = pl_str + str_p
            if tmr == 50:
                idx = 22

        elif idx == 20:  # Potion
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("Potion!")
                #se[2].play()
            if tmr == 6:
                pl_life = pl_lifemax
                potion = potion - 1
            if tmr == 11:
                idx = 13
                tmr = 0

        elif idx == 21:  # Blaze gem
            draw_battle(screen, fontS)
            img_rz = pygame.transform.rotozoom(imgEffect[1], 30 * tmr, (12 - tmr) / 8)
            X = 440 - img_rz.get_width() / 2
            Y = 360 - img_rz.get_height() / 2
            screen.blit(img_rz, [X, Y])
            if tmr == 1:
                set_message("Blaze gem!")
                #se[1].play()
            if tmr == 6:
                blazegem = blazegem - 1
            if tmr == 11:
                dmg = 1000
                idx = 12
                tmr = 4

        elif idx == 22:  # 戦闘終了
            #pygame.mixer.music.load("sound/ohd_bgm_field.ogg")
            #pygame.mixer.music.play(-1)
            idx = 1

        draw_text(screen, "[S]peed " + str(speed), 740, 40, fontS, WHITE)
        pygame.display.update()
        clock.tick(4 + 2 * speed)

if __name__ == '__main__':
    main()