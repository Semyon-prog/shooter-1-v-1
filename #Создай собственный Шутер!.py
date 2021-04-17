#Шутер 1 на 1
from pygame import *
from random import randint
from time import time as timer

window = display.set_mode((700, 500))
life1 = 3
life2 = 3

font.init()
font1 = font.SysFont("Arial", 60)
lose1 = font1.render("PLAYER 2 WIN", True, (180, 0, 0))
lose2 = font1.render("PLAYER 1 WIN", True, (180, 0, 0))

font2 = font.SysFont("Areal", 36)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.y = player_y
        self.rect.x = player_x

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def update2(self):
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire1(self):
        bullet = Bullet('bullet.png', self.rect.centerxy, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
    def fire2(self):
        bullet = Bullet('bullet.png', self.rect.centery, self.rect.top, 685, 20, -15)
        bullets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter1v1")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))
player1 = Player('rocket.png', win_height - 30, 200, 4, 50, 150)
player2 = Player('rocket.png', win_height - 520, 200, 4, 50, 150)

bullets = sprite.Group()

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

run = True
finish = False
rel_time1 = False
rel_time2 = False
num_fire1 = 0
num_fire2 = 0

clock = time.Clock()
FPS = 60

font.init()
font = font.SysFont("Arial", 70)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_RCTRL:
                if num_fire1 < 5 and rel_time1 == False:
                    num_fire1 = num_fire1 + 1
                    fire_sound.play()
                    player1.fire() 

                if num_fire1 >= 5 and rel_time1 == False:
                    last_time1 = timer()
                    rel_time1 = True

        elif e.type == KEYDOWN:
            if e.key == K_TAB:
                if num_fire2 < 5 and rel_time2 == False:
                    num_fire2 = num_fire2 + 1
                    fire_sound.play()
                    player2.fire() 

                if num_fire2 >= 5 and rel_time2 == False:
                    last_time2 = timer()
                    rel_time2 = True


    if sprite.spritecollide(player1, bullets, False):
        sprite.spritecollide(player1, bullets, True)
        finish = True
        window.blit(lose1, (100, 200))
        lost_lifes

    if sprite.spritecollide(player2, bullets, False):
        sprite.spritecollade(player2, bullets, True)
        finish = True
        window.blit(lose2, (100, 200))
        lost_lifes

    if finish != True:
        window.blit(background, (0, 0))
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        bullets.update()  
        bullets.draw(window)

        if sprite.spritecollide(player1, bullets, False):
            sprite.spritecollide(player1, bullets, True)
            life1 = life1 - 1
        if life1 == 0:
            finish = True
            window.blit(lose1, (200, 200))
        if rel_time1 == True:
            now_time1 = timer()
            if now_time1 - last_time1 < 3:
                reload1 = font2.render('Pl 1 reloading...', 1, (255, 255, 255))
                window.blit(reload1, (260,460))
            else:
                num_fire1 = 0
                rel_time1 = False
        if life1 == 3:
            life_color = (0, 150, 0)
        if life1 == 2:
            life_color = (150, 150, 0)
        if life1 == 1: 
            life_color = (150, 0, 0)
        text_life1 = font1.render(str(life1), 1, life_color)
        window.blit(text_life1, (650, 10))

        if sprite.spritecollide(player2, bullets, False):
            sprite.spritecollide(player2, bullets, True)
            life2 = life2 - 1
        if life2 == 0:
            finish = True
            window.blit(lose2, (200, 200))
        if rel_time2 == True:
            now_time2 = timer()
            if now_time2 - last_time2 < 3:
                reload2 = font2.render('Pl 2 reloading...', 1, (255, 255, 255))
                window.blit(reload2, (240,460))
            else:
                num_fire2 = 0
                rel_time2 = False
        if life2 == 3:
            life_color = (0, 150, 0)
        if life2 == 2:
            life_color = (150, 150, 0)
        if life2 == 1: 
            life_color = (150, 0, 0)
        text_life2 = font1.render(str(life2), 1, life_color)
        window.blit(text_life2, (100, 10))
    else:
        finish = False
        num_fire1 = 0
        life1 = 3
        num_fire2 = 0
        life2 = 3
        for b in bullets:
            b.kill()
        
        time.delay(3000)
    display.update()
    time.delay(20)