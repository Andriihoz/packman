from pygame import *
from pygame.sprite import collide_rect
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

window_width = 500
window_height = 600
window = display.set_mode((window_width,window_height))
background = scale(load('fon-zadnii-pakmen.jpg'),(window_width,window_height))

class GameSprite(sprite.Sprite):
    def __init__(self,image,x,y,speed):
        super().__init__()
        self.image = scale(load(image),(35,35))
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
        if keys[K_DOWN] and self.rect.y < window_height - 80:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < window_width - 80:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def __init__(self, image, x, y, speed):
        super().__init__(image, x, y, speed)
        self.direction = 'down'

    def update(self):
        pass

    def move_up_down(self):
        if self.direction == 'down':
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

        if self.rect.y <= 15:
            self.direction = 'down'
        if self.rect.y >= 500:
            self.direction = 'up'
        
    def move_right_left(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        if self.rect.x <= 15:
            self.direction = 'right'
        if self.rect.x >= 480:
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

wall1 = Wall('wall.png', 134, 128,20,138)
wall2 = Wall('wall.png', 347, 125,20,138)
wall3 = Wall('wall.png', 241, 126,20,77)
wall4 = Wall('wall.png', 241, 126,20,77)
wall5 = Wall('wall.png', 241, 126,20,77)
wall6 = Wall('wall.png', 241, 126,20,77)
wall7 = Wall('wall2.jpg', 241, 127,20,77)

walls = sprite.Group()
walls.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7)

pacman = Player('pngwing.com.png',100,420,4)
ghost1 = Enemy('pngwing.com (2).png',200,270,2)
ghost2 = Enemy('pngwing.com (3).png',100,15,2)
ghost3 = Enemy('ghost3.png',15,90,2)

game = True
finish = False

clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    if not finish:
        window.blit(background,(0,0))
        pacman.reset()
        #ghost1.reset()
        ghost2.move_up_down()
        ghost2.reset()
        ghost3.move_right_left()
        ghost3.reset()
        walls.draw(window)

    pacman.update()
    #ghost1.update()
    ghost2.update()
    ghost3.update()
    display.update()
    clock.tick(FPS)
