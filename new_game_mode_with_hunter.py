import random

import pygame as pg
import pygame.font

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


arrow_img = pg.image.load('imgs/arrow.png')
img = pygame.transform.rotate(arrow_img, 180)

current_hunter_position = 0


# urobit to iba s jednym sipom
class Arrow:
    # arrow x = player x
    def __init__(self):
        self.num_of_arrows = 6
        self.img = pg.image.load('imgs/arrow.png')
        self.y = 0
        self.arrow_img_array = []
        self.arrow_pos_y_array = []
        self.arrow_pos_x_array = []
        self.position = 1
        self.state = 'unready'
        self.img = pygame.transform.rotate(self.img, 180)
        self.dead_lion = pg.image.load('imgs/dead_lion.png')
        self.img_size = (64, 64)
        self.dead_lion = pg.transform.scale(self.dead_lion, self.img_size)
        self.value = 0

    #################################################

    # one arrow firing

    def check_pos(self):
        if self.y < 800 - 64 and self.y > 0:
            self.state = 'unready'
            return self.state
        else:
            self.y = self.value
            self.state = 'ready'
            return self.state

    def show_one_arrow(self, x):
        screen.blit(self.img, (x, self.y))

    def detect_collision(self):
        if player.player_pos_x > current_hunter_position + 10 and player.player_pos_x < current_hunter_position + 60 and player.player_pos_y > self.y + 10 and player.player_pos_y < self.y + 60 or player.player_pos_x + 64 > current_hunter_position + 10 and player.player_pos_x < current_hunter_position + 60 and player.player_pos_y + 60 > \
                self.y + 10 and player.player_pos_y < self.y + 60:
            print('collision detecalseted')
            player.player_img = self.dead_lion
            #screen.blit(self.dead_lion, (player.player_pos_x, player.player_pos_y))
            hunter.hunter_pos_y = -2222
            hunter.player_pos_x = -2222
            self.value = -2222
            pg.display.update()
            return False

    def move_arrow(self):
        self.y += random.randint(6, 15)

    ################################################
    def init_arrows(self):
        for i in range(self.num_of_arrows):
            self.arrow_img_array.append(self.img)
            self.arrow_pos_y_array.append(self.y)
            self.arrow_pos_x_array.append(0 - 64)

    # only shownig def
    def show_arrow(self):
        screen.blit(self.arrow_img_array[self.position],
                    (self.arrow_pos_x_array[self.position], self.arrow_pos_y_array[self.position]))
        self.position += 1
        if self.position == 6:
            self.position = 0

    # arrow movement
    def arrow_move(self):
        # screen.blit(img, (x, self.y))
        self.y += 2


arrow = Arrow()


# hunter class
class Hunter():
    def __init__(self):
        self.hunter_pos_x = 0
        self.hunter_pos_y = 0
        self.hunter_img = pg.image.load('imgs/caveman.png')
        self.arrow_image = pg.image.load('imgs/arrow.png')
        # arrow section

    # showing hunter
    def show(self):
        screen.blit(self.hunter_img, (self.hunter_pos_x, self.hunter_pos_y))

    # moving hunter on the ground
    def move(self):
        self.hunter_pos_x += 5
        if self.hunter_pos_x + 128 > 800:
            self.hunter_pos_x = 0

    def show_arrow(self, x, y):
        screen.blit(self.arrow_image, (x, y))
        pg.display.update()

    # hunter fire arrow
    def fire_arrow(self):
        arrow_x = self.hunter_pos_x
        arrow_y = 128
        a = random.randint(0, 2)
        print(f'a is {a}')
        if a == 1:
            screen.blit(self.arrow_image, (arrow_x, arrow_y))


hunter = Hunter()

background_img = pg.image.load('imgs/savana3.png')
# bomb = Bomb(Bomb.bomb_y_ar, Bomb.bomb_x_ar, Bomb.bomb_img_ar, Bomb.num_of_bombs)
bns = Bonus()
player = Player(Player.player_pos_y, Player.player_pos_x, Player.player_img, Player.change_img_pos_x,
                Player.change_img_pos_y)

# do it by arrow (not bomb.detect_collision())

b = True

while not arrow.detect_collision():
    # funcs must be run: hunter_show, hunter_move, hunter_fire_arrow, show_player, player_move, bonus...
    screen.fill((0, 0, 0))
    screen.blit(background_img, (0, 0))

    # mouse movement test
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(f'mouse pos is:{mouse_x, mouse_y}')


    hunter.show()
    hunter.move()

    ###################

    if arrow.check_pos() == 'ready':
        current_hunter_position = hunter.hunter_pos_x
        arrow.show_one_arrow(current_hunter_position)
        arrow.move_arrow()
    else:
        arrow.detect_collision()
        arrow.move_arrow()
        arrow.show_one_arrow(current_hunter_position)

    ###################

    # arrow.show_arrow()
    # arrow.arrow_move()

    player.show_player()
    player.move()

    text.show_text(f'norm: {player.boost_charges}', 750, 700)
    text.show_text(f'mega: {player.mega_boost_charges}', 750, 650)

    bns.spawn_cake()
    bns.cake_move()
    bns.detect_collision()

    pg.display.update()
