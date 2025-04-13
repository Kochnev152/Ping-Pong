#Создай собственный Шутер!

from pygame import *

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
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x >= 10:
            self.rect.x -= 10
        if keys_pressed[K_RIGHT] and self.rect.x <= 620:
            self.rect.x += 10
        if keys_pressed[K_UP] and self.rect.y >= 10:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and self.rect.y <= 420:
            self.rect.y += 10