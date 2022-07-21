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


class Bonus:

    def __init__(self):
        self.bonus_img = pg.image.load('imgs/cupcake.png')
        self.y = 0
        self.x = random.randint(0, 900 - 32)
        self.speed = 1

    def spawn_cake(self):
        screen.blit(self.bonus_img, (self.x, self.y))

    def cake_move(self):
        self.y += self.speed
        if self.y > 800:
            self.y = 0
            self.x = random.randint(0, 900 - 64)

    def detect_collision(self):
        if player.player_pos_x > self.x and player.player_pos_x < self.x + 32 and player.player_pos_y > self.y and player.player_pos_y < self.y + 32 or player.player_pos_x + 64 > self.x and player.player_pos_x + 64 < self.x + 32 and player.player_pos_y + 64 > self.y and player.player_pos_y + 64 < self.y + 32:
            player.boost_charges += 1
            self.y = 0
            self.x = random.randint(0, 900 - 64)
            self.speed += 0.5

    # background img

arrow_img = pg.image.load('imgs/arrow.png')
class Arrow:
    def __init__(self):
        self.num_of_arrows = 8
        self.arrow_img_array = []
        self.arrow_pos_y_array = []

        self.arrow_img = pg.image.load('imgs/arrow.png')
        pass

    def detect_collision(self):
        pass

    def return_img(self):
        return self.arrow_img

    def add_arrows(self):
        for i in range(self.num_of_arrows):
            self.arrow_img_array.append(self.arrow_img)
            self.arrow_pos_y_array.append(128)


arrow = Arrow()
arrow.add_arrows()


class Hunter():
    def __init__(self):
        self.hunter_pos_x = 0
        self.hunter_pos_y = 0
        self.hunter_img = pg.image.load('imgs/caveman.png')
        self.arrow_image = pg.image.load('imgs/arrow.png')

    def hunter_move_and_fire_arrow(self):
        self.hunter_pos_x = random.randint(0, 900 - 128)

        screen.blit(self.arrow_image, (self.hunter_pos_x, 128))

    def show_hunter(self):
        screen.blit(self.hunter_img, (self.hunter_pos_x, self.hunter_pos_y))

    def show_arrow(self):
        z = 0
        if z == 9:
            z = 0
        screen.blit(self.arrow_image, (hunter.hunter_pos_x, arrow.arrow_pos_y_array[z]))

        z += 1

    def move_arrows(self):
        for q in range(arrow.num_of_arrows):
          screen.blit(arrow.arrow_img_array[q], (hunter.hunter_pos_x, arrow.arrow_pos_y_array[q]))
          arrow.arrow_pos_y_array[q] = arrow.arrow_pos_y_array[q] + 5


hunter = Hunter()

background_img = pg.image.load('imgs/savana3.png')
# bomb = Bomb(Bomb.bomb_y_ar, Bomb.bomb_x_ar, Bomb.bomb_img_ar, Bomb.num_of_bombs)
bns = Bonus()
player = Player(Player.player_pos_y, Player.player_pos_x, Player.player_img, Player.change_img_pos_x,
                Player.change_img_pos_y)

# do it by arrow (not bomb.detect_collision())
count = 0
while True:
    # if bomb.detect_collision():
    #   bomb.show_bomb_explosion()
    if count % 30 == 0:
        print(f'count is :{count}')
        hunter.hunter_move_and_fire_arrow()
        hunter.show_arrow()
        pg.display.update()



    hunter.move_arrows()

    screen.fill((0, 0, 0))

    screen.blit(background_img, (0, 0))

    player.move()

    player.show_player()

    hunter.show_hunter()

    text.show_text(f'norm: {player.boost_charges}', 750, 700)
    text.show_text(f'mega: {player.mega_boost_charges}', 750, 650)

    bns.spawn_cake()
    bns.cake_move()
    bns.detect_collision()

    count = count + 1
    print(count)
    pg.display.update()
