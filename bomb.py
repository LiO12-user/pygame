import pygame as pg
import random
import time

import pygame.font
from pygame import mixer



class Bomb:
    def bomb(self, speed, bomb_x, bomb_y, bomb_img):
        self.speed = speed
        self.bomb_x = bomb_x
        self.bomb_y = bomb_y
        self.bomb_img = bomb_img

