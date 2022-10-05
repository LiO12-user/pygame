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
                    self.boost_charges -= self.val3  # 1

                if event.key == pg.K_DELETE:
                    self.change_img_pos_x *= self.val2
                    self.change_img_pos_y *= self.val2
                    self.mega_boost_charges -= self.val4  # 1

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
