import pygame as pg

pg.init()

screen = pg.display.set_mode((900, 800))
img = pg.image.load('imgs/cupcake.png')
screen.blit(img, (200, 200))
while True:
    pg.display.update()
