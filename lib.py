import pygame as pg
import random as rn
pg.init()
screen = pg.display.set_mode((500, 500))
bg = pg.Surface(screen.get_size())
bg.fill((255, 255, 255))
background = pg.image.load('wall.png')
background_rect = background.get_rect()
player_img = pg.image.load('cutecat.png')
Wall_img = pg.image.load('wall.png')

WIDTH = 480
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.radius = 20
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -1
        if keystate[pg.K_RIGHT]:
            self.speedx = 1
        if keystate[pg.K_UP]:
            self.speedy = -1
        if keystate[pg.K_DOWN]:
            self.speedy = 1
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.left > HEIGHT:
            self.rect.left = HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0

class Wall(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = Wall_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = rn.randint(0, 470)
        self.rect.y = rn.randint(0, 470)

all_sprites = pg.sprite.Group()
walls = pg.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Wall()
    all_sprites.add(m)
    walls.add(m)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    all_sprites.update()

    if pg.sprite.spritecollide(player, walls, False, pg.sprite.collide_rect):
        running = False

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pg.display.flip()
pg.quit()
