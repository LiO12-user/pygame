import pygame as pg
import random
import time

import pygame.font
from pygame import mixer

pg.init()




class Game:
    def __init__(self):
        self.run_again = True

    def set_true(self):
        self.run_again = True
        return self.run_again

    def set_false(self):
        self.run_again = False
        return self.run_again


game = Game()

class Screen:

    def __init__(self):
        self.x = 900
        self.y = 800

    def set_mode(self):
        screen = pg.display.set_mode((self.x, self.y))
        return screen

# init screen
s = Screen()
screen = s.set_mode()

class Texts:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def show_text(self, text, x, y):
        over_text = self.font.render(str(text), True, (255, 255, 255))
        screen.blit(over_text, (x, y))

text = Texts()

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
        self.boost_charges = 5
        self.mega_boost_charges = 2
        self.val = 4
        self.val2 = 8
        self.val3 = 1
        self.val4 = 1


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

                if event.key == pg.K_SPACE:
                    self.change_img_pos_x *= self.val
                    self.change_img_pos_y *= self.val
                    self.boost_charges -= self.val3 #1

                if event.key == pg.K_DELETE :
                    self.change_img_pos_x *= self.val2
                    self.change_img_pos_y *= self.val2
                    self.mega_boost_charges -= self.val4 #1

                if self.boost_charges <= 0:
                    self.val = 1
                    self.val3 = 0

                if self.mega_boost_charges <= 0:
                    self.val2 = 1
                    self.val4 = 0

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
        self.speed = random.randint(1, 5)
        self.last_bomb_posx = 0
        self.last_bomb_posy = 0
        self.index = 0

    def add_bombs(self):
        for k in range(self.num_of_bombs):
            self.bomb_img_ar.append(pg.image.load('imgs/bomb.png'))
            self.bomb_y_ar.append(0)
            self.bomb_x_ar.append(random.randint(0, 900 - 64))

    def show_bomb_explosion(self):
        self.bomb_img_ar[self.index] = pg.image.load('imgs/nuclear-explosion.png')
        screen.blit(self.bomb_img_ar[self.index], (self.last_bomb_posx, self.last_bomb_posy))
        pg.display.update()
        time.sleep(1)


    def detect_collision(self):
        for l in range(6):
           if player.player_pos_x > self.bomb_x_ar[l]+10 and player.player_pos_x < self.bomb_x_ar[l] + 60 and player.player_pos_y > self.bomb_x_ar[l]+10 and player.player_pos_y < self.bomb_y_ar[l]+60 or player.player_pos_x+64 > self.bomb_x_ar[l]+10 and player.player_pos_x < self.bomb_x_ar[l]+60 and player.player_pos_y +60 > self.bomb_y_ar[l]+10 and player.player_pos_y < self.bomb_y_ar[l]+60:
                print('collision')
                print(f'p y {player.player_pos_y}')
                print(f'p x {player.player_pos_x}')
                print(f'b y {bomb.bomb_y_ar[l]}')
                print(f'b x {bomb.bomb_x_ar[l]}')

                self.speed = 0
                self.last_bomb_posx = self.bomb_x_ar[l]
                self.last_bomb_posy = self.bomb_y_ar[l]
                self.index = l

                for j in range(self.num_of_bombs):
                    self.bomb_x_ar[j] = -2000
                    screen.blit(self.bomb_img_ar[j], (self.bomb_x_ar[j], self.bomb_y_ar[j]))
                    pg.display.update()

                return game.set_true()
        return game.set_false()

    def show_bombs(self):
        for i in range(self.num_of_bombs):
            screen.blit(self.bomb_img_ar[i], (self.bomb_x_ar[i], self.bomb_y_ar[i]))
            self.bomb_y_ar[i] += random.randint(1, 5)


    def check_bomb_pos_y(self):
        for i in range(self.num_of_bombs):
            if self.bomb_y_ar[i] > 800 - 64:
                self.bomb_y_ar[i] = 0
                self.bomb_x_ar[i] = 0
                self.bomb_x_ar[i] = random.randint(0, s.x - 64)
                print(f'bomb x pos is {self.bomb_x_ar[i]}')
                print(self.bomb_y_ar[i])

    def check_bomb_pos_x(self):
        for i in range(self.num_of_bombs):

            sorted = self.bomb_x_ar.sort()
            min = sorted[:1]
            max = sorted[-1]


# background img
background_img = pg.image.load('imgs/savana3.png')

bomb = Bomb(Bomb.bomb_y_ar, Bomb.bomb_x_ar, Bomb.bomb_img_ar, Bomb.num_of_bombs)
player = Player(Player.player_pos_y, Player.player_pos_x, Player.player_img, Player.change_img_pos_x,  Player.change_img_pos_y)

if __name__ == "__main__":
    bomb.add_bombs()

while not bomb.detect_collision():

    if bomb.detect_collision():
        bomb.show_bomb_explosion()

    screen.fill((0, 0, 0))

    screen.blit(background_img, (0, 0))

    player.move()

    player.show_player()

    bomb.show_bombs()

    bomb.check_bomb_pos_y()

    text.show_text(f'norm: {player.boost_charges}', 750, 700)
    text.show_text(f'mega: {player.mega_boost_charges}', 750, 650)

    pg.display.update()

