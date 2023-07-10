
import pygame
from spritesheet import SpriteSheet

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.file = SpriteSheet("sprites.png")
        self.image = self.file.parse_sprite("key1.png")
        self.rect = self.image.get_rect(center=pos)
        self.z = 7
        #self.collision_sprites = collision_sprites

        self.speed = 300
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(self.rect.center)
        self.direction.x = 1

    
    def move(self,dt):
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = round(self.pos.x)

    def update(self,dt):
        self.move(dt)