import pygame as pg
import random
import time

import pygame.font
from pygame import mixer

pg.init()

y = 800  # vyska
x = 900  # sirka

screen = pg.display.set_mode((x, y))

class Player:
    player_img = pg.image.load('imgs/lion.png')
    change_img_pos_y = 0
    change_img_pos_x = 0
    player_pos_y = 800 - 64
    player_pos_x = 900 - 64


    def __init__(self, pos_y, pos_x, img, change_img_pos_x, change_img_pos_y):
        self.player_pos_y = pos_y
        self.player_pos_x = pos_x
        self.player_img = img
        self.change_img_pos_x = change_img_pos_x
        self.change_img_pos_y = change_img_pos_y


    def show_player(self):
        screen.blit(self.player_img, (self.player_pos_x, self.player_pos_y))

    def move(self):
        for event in pg.event.get():
            # player movement
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.change_img_pos_x = -5
                if event.key == pg.K_RIGHT:
                    self.change_img_pos_x = 5
                if event.key == pg.K_UP:
                    self.change_img_pos_y = -5
                if event.key == pg.K_DOWN:
                    self.change_img_pos_y = 5
            if event.type == pg.KEYUP:
                if event.type == pg.K_LEFT or pg.K_RIGHT:
                    self.change_img_pos_x = 0
                    self.change_img_pos_y = 0

        self.player_pos_x += self.change_img_pos_x
        self.player_pos_y += self.change_img_pos_y

        if self.player_pos_x >= 836:
            self.player_pos_x = 836

        if self.player_pos_x <= 0:
            self.player_pos_x = 0

        if self.player_pos_y >= 733:
            self.player_pos_y = 733

        if self.player_pos_y <= 0:
            self.player_pos_y = 0


class Bomb:
    bomb_x_ar = []
    bomb_y_ar = []
    bomb_img_ar = []
    num_of_bombs = 6

    b_img = pg.image.load('imgs/bomb.png')

    def __init__(self, bomb_y, bomb_x, bomb_img, nums_of_bombs):
        self.bomb_y_ar = bomb_y
        self.bomb_x_ar = bomb_x
        self.bomb_img_ar = bomb_img
        self.num_of_bombs = nums_of_bombs
        self.speed = random.randint(1, 6)

    def add_bombs(self):
        for k in range(self.num_of_bombs):
            self.bomb_img_ar.append(pg.image.load('imgs/bomb.png'))
            self.bomb_y_ar.append(0)
            self.bomb_x_ar.append(random.randint(0, 900 - 64))

    def show_bomb_explosion(self):
        self.bomb_img_ar[self.i] = pg.image.load('imgs/nuclear-explosion.png')
        screen.blit(self.bomb_img_ar[self.i], (self.bomb_x_ar[self.i], self.bomb_y_ar[self.i]))
        pg.display.update()

    def detect_collision(self):
        for l in range(6):
            print(self.num_of_bombs)
            print(l)

            if Player.player_pos_x > self.bomb_x_ar[l] and Player.player_pos_x < self.bomb_x_ar[l] + 64 and Player.player_pos_y > self.bomb_x_ar[l] and Player.player_pos_y < self.bomb_y_ar[l]+64 or Player.player_pos_x+64 > self.bomb_x_ar[l] and Player.player_pos_x < self.bomb_x_ar[l]+64 and Player.player_pos_y +64 > self.bomb_y_ar[l] and Player.player_pos_y < self.bomb_y_ar[l]+64:
                print('collision')
                self.speed = 0

                for j in range(self.num_of_bombs):
                    self.bomb_x_ar[j] = -2000
                    # despawn bombs
                    screen.blit(self.bomb_img_ar[j], (self.bomb_x_ar[j], self.bomb_y_ar[j]))
                    pg.display.update()





    def test(self):
        for i in range(self.num_of_bombs):
            if self.bomb_y_ar[i] < Player.player_pos_y and self.bomb_y_ar[i] + 63 > Player.player_pos_y and self.bomb_x_ar[i] < Player.player_pos_x and self.bomb_x_ar[
                i] + 63 > Player.player_pos_x or Player.player_pos_y + 63 > self.bomb_y_ar[i] and Player.player_pos_y < self.bomb_y_ar[i] + 63 and Player.player_pos_x + 63 > \
                    self.bomb_x_ar[i] and Player.player_pos_x < self.bomb_x_ar[i] + 63:

                for j in range(self.num_of_bombs):
                    self.bomb_x_ar[j] = -2000
                    # despawn bombs
                    screen.blit(self.bomb_img_ar[j], (self.bomb_x_ar[j], self.bomb_y_ar[j]))
                    pg.display.update()



    def show_bombs(self):
        for i in range(self.num_of_bombs):
            screen.blit(self.bomb_img_ar[i], (self.bomb_x_ar[i], self.bomb_y_ar[i]))
            self.bomb_y_ar[i] += self.speed


    def check_bomb_pos_y(self):
        if self.bomb_y_ar[self.num_of_bombs - 1] >= x - 64:
            self.num_of_bombs += 1


# background img
background_img = pg.image.load('imgs/savana3.png')

# nuclear explosion img
exp_img = pg.image.load('imgs/nuclear-explosion.png')

bomb = Bomb(Bomb.bomb_y_ar, Bomb.bomb_x_ar, Bomb.bomb_img_ar, Bomb.num_of_bombs)
player = Player(Player.player_pos_y, Player.player_pos_x, Player.player_img, Player.change_img_pos_x,  Player.change_img_pos_y)

if __name__ == "__main__":
    bomb.add_bombs()

while True:

    bomb.test()

    screen.fill((0, 0, 0))

    screen.blit(background_img, (0, 0))

    player.move()

    player.show_player()

    bomb.show_bombs()


    pg.display.update()

