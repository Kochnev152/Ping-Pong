#Создай собственный Шутер!

from pygame import *
clock = time.Clock()
FPS = 60
window = display.set_mode((700,500))
name = display.set_caption('Ping-Pong')
background = transform.scale(image.load('mountain.jpg'),(700,500))
x_random = randint(50,630)
player__x = 300
player = Player('rocket.png',player__x,400,0)
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,size_x=65,size_y=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = size_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    def collidepoint(self):
        return self.rect.collidepoint()
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
            
    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed

window = display.set_mode((700,500))
name = display.set_caption('Ping-Pong')
background = transform.scale(image.load('mountain.jpg'),(700,500))
ball_x = 350
ball_y = 250
ball_x_speed = 5
ball_y_speed = 5
player_1 = Player('racket.png',10,250,5,80,80)
player_2 = Player('racket.png',690,250,5,80,80)
ball = Player('tennis.png',ball_x,ball_y,5,80,80)
game = True
finish = False
font.init()

font_loser = font.Font('Arial', 60)
font = font.Font('Arial', 36)
loser = font_loser.render('Игрок 1 проиграл', True, (255,0,0))
winner = font_loser.render('Игрок 2 проиграл', True, (0,255,0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.blit(background, (0,0))
        player_1.update_1()
        player_2.update_2()
        ball.rect.x += ball_x_speed
        ball.rect.y += ball_y_speed
        if ball.colliderect(player_1.rect):
            ball_x_speed *= -1
        if ball.rect.y > 420 or ball.rect < 80:
            ball_y_speed *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(loser, (200,200))
        if ball.rect.x > 500:
            finish = True
            window.blit(winner, (200,200))
        player_1.reset()
        player_2.reset()
        
clock.tick(FPS)
display.update()
        
