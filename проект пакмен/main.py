from pygame import *
from pygame.sprite import collide_rect
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

points = 7
window_width = 500
window_height = 600
window = display.set_mode((window_width,window_height))
background = scale(load('fon-zadnii-pakmen.png'),(window_width,window_height))

class GameSprite(sprite.Sprite):
    def __init__(self,image,x,y,speed):
        super().__init__()
        self.image = scale(load(image),(26,26))
        self.speed = speed

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
            if sprite.spritecollide(self,walls,False):
                self.rect.y += self.speed
        if keys[K_DOWN] and self.rect.y < window_height - 80:
            self.rect.y += self.speed
            if sprite.spritecollide(self,walls,False):
                self.rect.y -= self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
            if sprite.spritecollide(self,walls,False):
                self.rect.x += self.speed
        if keys[K_RIGHT] and self.rect.x < window_width - 80:
            self.rect.x += self.speed
            if sprite.spritecollide(self,walls,False):
                self.rect.x -= self.speed

class Enemy(GameSprite):
    def __init__(self, image, x, y, speed):
        super().__init__(image, x, y, speed)
        self.direction = 'down'

    def update(self):
        pass

    def move_up_down(self,min_x,max_x):
        if self.direction == 'down':
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

        if self.rect.y <= min_x:
            self.direction = 'down'
        if self.rect.y >= max_x:
            self.direction = 'up'
        
    def move_right_left(self,min_y,max_y):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        if self.rect.x <= min_y:
            self.direction = 'right'
        if self.rect.x >= max_y:
            self.direction = 'left'

class Wall(sprite.Sprite):
    def __init__(self,image,x,y,wall_width,wall_height):
        super().__init__()
        self.image = scale(load(image),(wall_width,wall_height))
        self.width = wall_width
        self.height = wall_height

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))  

wall1 = Wall('wall6.png', 135, 128,20,138)
wall2 = Wall('wall8.png', 347, 125,20,138)
wall3 = Wall('wall9.png', 293, 185,75,20)
wall4 = Wall('wall10.png', 136, 185,71,20)

wall5 = Wall('wall3.png', 188, 128,128,20)
wall7 = Wall('wall2.png', 241, 128,20,77)
wall6 = Wall('wall3.png', 188, 360,124,20)
wall8 = Wall('wall2.png', 241, 359,20,77)
wall9 = Wall('wall3.png', 188, 475,128,20)
wall10 = Wall('wall2.png', 241, 474,20,77)

wall11 = Wall('wall4.png', 45, 127,55,20)
wall12 = Wall('wall4.png', 401, 129,55,20)
wall13 = Wall('wall4.png', 295, 50,73,40)
wall14 = Wall('wall4.png', 400, 50,55,40)

wall15 = Wall('wall7.png', 45, 50,55,40)
wall16 = Wall('wall7.png', 136, 50,73,40)
wall17 = Wall('wall7.png', 295, 50,73,40)
wall18 = Wall('wall7.png', 400, 50,55,40)

wall19 = Wall('wall.png', 134, 302,25,75)
wall20 = Wall('wall.png', 343, 302,25,75)
wall21 = Wall('wall7.png', 295, 50,73,40)
wall22 = Wall('wall7.png', 400, 50,55,40)

wall23 = Wall('wall4.png', 134, 417,73,20)
wall24 = Wall('wall4.png', 292, 417,73,20)

wall25 = Wall('wall11.png', 80, 417,20,80)
wall26 = Wall('wall12.png', 46, 417,55,20)

wall27 = Wall('wall13.png', 400, 417,20,80)
wall28 = Wall('wall14.png', 400, 417,55,20)

wall29 = Wall('wall15.png', 46, 533,161,20)
wall30 = Wall('wall16.png', 295, 533,161,20)
wall31 = Wall('wall17.png', 133, 476,20,77)
wall32 = Wall('wall17.png', 347, 476,20,77)

wall33 = Wall('wall21.png', 188, 310,125,10)
wall34 = Wall('wall22.png', 303, 242,10,79)
wall35 = Wall('wall23.png', 188, 243,10,77)
wall36 = Wall('wall24.png', 269, 243,44,10)
wall37 = Wall('wall25.png', 189, 243,44,10)

wall38 = Wall('wall19.png', 1, 474,44,20)
wall39 = Wall('wall20.png', 455, 474,44,20)

wall40 = Wall('wall26.png', 0, 0,500,20)
wall41 = Wall('wall27.png', 0, 0,15,205)
wall42 = Wall('wall28.png', 493, 0,15,205)

wall43 = Wall('wall18.png', 241, 2,20,86)

wall44 = Wall('wall29.png', 0, 184,100,80)
wall45 = Wall('wall30.png', 0, 302,100,80)
wall46 = Wall('wall31.png', 400, 184,100,80)
wall47 = Wall('wall32.png', 400, 302,100,80)
wall48 = Wall('wall33.png', 0, 370,15,230)
wall49 = Wall('wall34.png', 490, 370,15,230)
wall50 = Wall('wall35.png', 0, 600,500,20)









walls = sprite.Group()
walls.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16,wall17,wall18,wall19,wall20,wall21,wall22,wall23,wall24,wall25,wall26,wall27,wall28,wall29,wall30,wall31,wall32,wall33,wall34,wall35,wall36,wall37,wall38,wall39,wall40,wall41,wall42,wall43,wall44,wall45,wall46,wall47,wall48,wall49,wall50)

pacman = Player('pngwing.com.png',250,280,4)
ghost1 = Enemy('pngwing.com (2).png',368,20,5)
ghost2 = Enemy('pngwing.com (3).png',100,15,5)
ghost3 = Enemy('ghost3.png',15,90,5)


ghosts = sprite.Group()
ghosts.add(ghost1,ghost2,ghost3)

coin1 = GameSprite('coins.png', 10, 188,0)
coin2 = GameSprite('coins.png', 135, 198,0)
coin3 = GameSprite('coins.png', 125, 168,0)
coin4 = GameSprite('coins.png', 139, 118,0)
coin5 = GameSprite('coins.png', 135, 178,0)
coin6 = GameSprite('coins.png', 165, 128,0)
coin7 = GameSprite('coins.png', 135, 208,0)

coins = sprite.Group()
coins.add(coin1,coin2,coin3,coin4,coin5,coin6,coin7)


game = True
finish = False

clock = time.Clock()
FPS = 60

font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
font2 = font.Font(None, 36)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    if not finish:
        window.blit(background,(0,0))
        walls.draw(window)
        pacman.reset()
        ghost1.move_up_down(15,500)
        ghost1.reset()
        ghost2.move_up_down(15,500)
        ghost2.reset()
        ghost3.move_right_left(15,460)
        ghost3.reset()
        walls.draw(window)
        coins.draw(window)

    pacman.update()
    ghost1.update()
    ghost2.update()
    ghost3.update()

    if sprite.spritecollide(pacman,coins,True):
        points-=1
    if points ==0:
        finish = True
        window.blit(win,(200,200))
    if sprite.spritecollide(pacman,ghosts,False):
        finish = True
        window.blit(lose,(200,200))

    display.update()
    clock.tick(FPS)



