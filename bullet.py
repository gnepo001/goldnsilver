
import pygame
from spritesheet import SpriteSheet

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos,group,direction):
        super().__init__(group)
        self.file = SpriteSheet("sprites.png")
        self.image = self.file.parse_sprite("bullet.png")
        self.rect = self.image.get_rect(center=pos)
        self.z = 7
        self.bullet_direction = direction
        #self.collision_sprites = collision_sprites

        self.speed = 400
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(self.rect.center)
        self.direction.x = 1
        self.direction.y = 1

    
    def move(self,dt):
        if self.bullet_direction == "right":
            self.pos.x += self.direction.x * self.speed * dt
            self.rect.centerx = round(self.pos.x)
        elif self.bullet_direction == "left":
            self.pos.x -= self.direction.x * self.speed * dt
            self.rect.centerx = round(self.pos.x)
        elif self.bullet_direction == "up":
            self.pos.y -= self.direction.y * self.speed * dt
            self.rect.centery = round(self.pos.y)
        elif self.bullet_direction == "down":
            self.pos.y += self.direction.y * self.speed * dt
            self.rect.centery = round(self.pos.y)

    def update(self,dt):
        self.move(dt)