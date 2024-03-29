
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
        self.collision_sprites = group

        self.speed = 350
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(self.rect.center)
        self.direction.x = 1
        self.direction.y = 1

        #self.hitbox = self.rect.copy().inflate((-64 ,-64))
        self.hitbox = self.rect.copy()
    
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
        self.collision()
        self.hitbox = self.rect.copy().inflate((-100,-92))

    def collision(self):
        #print(self.collision_sprites.sprites())
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite,'killable'):
                #print(sprite)
                if sprite.hitbox.colliderect(self.hitbox):
                    sprite.kill()
                    self.kill()

    def update(self,dt):
        self.move(dt)