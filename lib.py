import random
import pygame as pg
r = ['hor', 'ver']
pg.init()
screen = pg.display.set_mode((500, 500))
bg = pg.Surface(screen.get_size())
bg.fill((255, 255, 255))
kitten = pg.image.load('cutecat.png')
wallimage = pg.image.load('wall.png')
wall2image = pg.image.load('wall2.png')
wnse = 's'

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = kitten
        self.rect = [10, 10]



class Wall(pg.sprite.Sprite):
    def __init__(self):
        super(Wall, self).__init__()
        self.rotate = random.choice(r)
        if self.rotate == 'ver':
            self.image = wall2image
        elif self.rotate == 'hor':
            self.image = wallimage
        self.rect = (random.randint(10, 450), random.randint(10, 450))
    
pg.display.flip()
all_sprites = pg.sprite.Group()
walls = pg.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(20):
    m = Wall()
    all_sprites.add(m)
    walls.add(m)

r = True
while r:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            r = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP: wnse = 'up'
            if event.key == pg.K_DOWN: wnse = 'down'
            if event.key == pg.K_RIGHT: wnse = 'right'
            if event.key == pg.K_LEFT: wnse = 'left'
        elif event.type == pg.KEYUP: wnse = 's'
    if wnse == 'up':
        if 0 < player.rect[1] - 5 < 475:
            player.rect[1] -= 0.1
    elif wnse == 'down':
        if 0 < player.rect[1] + 5 < 475:
            player.rect[1] += 0.1
    elif wnse == 'right':
        if 0 < player.rect[0] + 5 < 475:
            player.rect[0] += 0.1
    elif wnse == 'left':
        if 0 < player.rect[0] - 5 < 475:
            player.rect[0] -= 0.1
    #if pg.sprite.collide_rect(player, walls):
    #    running = False

    screen.blit(bg, (0, 0))
    all_sprites.draw(screen)
    pg.display.flip()
pg.quit()








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
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] and self.rect.x-1>-10:
            self.speedx = -1
        if keystate[pg.K_RIGHT] and self.rect.x+1>460:
            self.speedx = 1
        if keystate[pg.K_UP] and self.rect.y-1>-10:
            self.speedy = -1
        if keystate[pg.K_DOWN] and self.rect.y+1>460:
            self.speedy = 1
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # if self.rect.right > WIDTH:
        #     self.rect.right = WIDTH
        # if self.rect.left < 0:
        #     self.rect.left = 0
        # if self.rect.y > HEIGHT:
        #     self.rect.left = HEIGHT
        # if self.rect.left < 0:
        #     self.rect.left = 0

class Wall(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = Wall_img
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
