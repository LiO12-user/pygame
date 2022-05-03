from array import array

import pygame as pg
import random
import time

import pygame.font
from pygame import mixer

pg.init()

y = 800  # vyska
x = 900  # sirka

screen = pg.display.set_mode((x, y))

# counter
counter = 0

# skakanie
# if img y + 64

pg.display.set_caption('lukas')
img_pos_x = 900-64  # #sirka
img_pos_y = 800-64  # vyska

change_img_pos_x = 400
change_img_pos_y = 800

# background img
background_img = pg.image.load('imgs/savana3.png')

# img props: width = 64, high = 64
img = pg.image.load('imgs/lion.png')

# nuclear explosion img
exp_img = pg.image.load('imgs/nuclear-explosion.png')

bomb_img = []
bomb_x = []
bomb_y = []
num_of_bombs = 6
z = num_of_bombs
k = num_of_bombs

can_show = True

# font
over_font = pygame.font.Font('freesansbold.ttf', 64)
again_font = pygame.font.Font('freesansbold.ttf', 32)


# initialize bombs into arrays
def init_bombs():
    for i in range(num_of_bombs):
        # bomb img
        bomb_img.append(pg.image.load('imgs/bomb.png'))

        # random bomb x pos
        bomb_x.append(random.randint(0, 900 - 64))

        # bomb y pos
        bomb_y.append(0)


# run init_bombs
init_bombs()


# change a bomb position
def change_bomb_position():
    for i in range(num_of_bombs):
        bomb_y[i] = 0
        bomb_x.clear()
        bomb_x[i] = random.randint(0, 900 - 64)


# show array state
def show_state():
    for o in range(num_of_bombs):
        print(len(bomb_y))
        print(len(bomb_x))
        print(len(bomb_img))


# show a lion
def player():
    screen.blit(img, (img_pos_x, img_pos_y))


# show a game over text
def show_game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (300, 350))


# show a again text
def show_game_again_text():
    over_text = again_font.render("PRESS SPACE BUTTON", True, (255, 255, 255))
    screen.blit(over_text, (300, 600))


def show_join_text():
    join_text = over_font.render("START GAME", True, (255, 255, 255))
    screen.blit(join_text, (300, 350))


# make a differend get down speed
speed = [1, 2, 4, 5, 10]


# show a bomb
def bomb(x, y, i):
    screen.blit(bomb_img[i], (x[i], y[i]))
    y[i] += speed[random.randint(0, 4)]


# music
music = mixer.music.load('background.wav')

# bomb spawning bool
can_spawn_bomb = True

# can add new bombs
can_add = True


# add new bomb
def add_new_bomb():
    bomb_y.append(0)
    bomb_x.append(random.randint(0, 900 - 64))
    bomb_img.append(pg.image.load('imgs/bomb.png'))


join = False

#####################################################

# easy starting page
while join == False:
    screen.fill((0, 0, 0))
    show_join_text()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print('shut down')

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print('game started')
                mixer.music.play(-1)
                join = True
    pg.display.update()

###################################################

# game booleans
game_shut_down = False
is_running = True

pg.display.update()

###################################################

while game_shut_down != True:
    while is_running:

        # collision detection
        for i in range(num_of_bombs):
            if bomb_y[i] < img_pos_y and bomb_y[i] + 63 > img_pos_y and bomb_x[i] < img_pos_x and bomb_x[
                i] + 63 > img_pos_x or img_pos_y + 63 > bomb_y[i] and img_pos_y < bomb_y[i] + 63 and img_pos_x + 63 > \
                    bomb_x[i] and img_pos_x < bomb_x[i] + 63:
                can_show = False

                for j in range(num_of_bombs):
                    bomb_x[j] = -2000
                    # despawn bombs
                    screen.blit(bomb_img[j], (bomb_x[j], bomb_y[j]))
                    pg.display.update()

                pg.display.update()
                mixer.music.stop()
                time.sleep(5)
                is_running = False

        screen.fill((0, 0, 0))

        screen.blit(background_img, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_shut_down = True
                is_running == False

            # player movement
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    change_img_pos_x = -5
                if event.key == pg.K_RIGHT:
                    change_img_pos_x = 5
                if event.key == pg.K_UP:
                    change_img_pos_y = -5
                if event.key == pg.K_DOWN:
                    change_img_pos_y = 5
            if event.type == pg.KEYUP:
                if event.type == pg.K_LEFT or pg.K_RIGHT:
                    change_img_pos_x = 0
                    change_img_pos_y = 0

        if img_pos_x >= 836:
            img_pos_x = 836

        if img_pos_x <= 0:
            img_pos_x = 0

        if img_pos_y >= 733:
            img_pos_y = 733

        if img_pos_y <= 0:
            img_pos_y = 0

        img_pos_x += change_img_pos_x
        img_pos_y += change_img_pos_y

        # shows a lion
        player()

        # spawn a bombs
        for i in range(num_of_bombs):
            bomb(bomb_x, bomb_y, i)

        # show bombs while not collision

        if can_show == True:
            for i in range(num_of_bombs):
                if bomb_y[i] > 800 - 64:
                    bomb_y[i] = 0
                    bomb_x[i] = 0
                    bomb_x[i] = random.randint(0, 900 - 64)

        counter += 1

        if can_add:
            if counter % 100 == 0:
                num_of_bombs += 1
                add_new_bomb()

        if counter >= 400:
            can_add = False

        pg.display.update()

    print('kkkkkkk')
    #################################################

    # again
    again = False
    while again == False:
        screen.fill((0, 0, 0))
        show_game_over_text()
        show_game_again_text()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                print('shut down')

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    is_running = True
                    again = True
                    mixer.music.play()
        pg.display.update()
