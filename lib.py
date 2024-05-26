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
