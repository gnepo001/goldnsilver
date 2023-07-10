import pygame

from spritesheet import SpriteSheet
from timer import Timer
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group,collision_sprites):
        super().__init__(group)
        self.group = group
        self.import_assets()
        self.frame_index = 0
        self.status = "idle"
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.z = 7
        self.collision_sprites = collision_sprites
        
        #collison
        #self.hitbox = self.rect.copy().inflate((-126,-70))
        self.hitbox = self.rect.copy().inflate((-30,-30))

        #movement
        self.direction = pygame.math.Vector2(self.rect.center)
        self.speed = 300
        self.pos = pygame.math.Vector2(self.rect.center)
        
        #maplocation
        self.location = "overworld"
        self.temp_pos = pygame.math.Vector2()
       
        #lives and health
        self.lives = 3
        self.health_status = "fine"

        self.hurt_timer = Timer(3000)
        self.shoot_timer = Timer(500)

    def import_assets(self):
        self.file = SpriteSheet("sprites.png")

        self.animations = {
            'idle':[self.file.parse_sprite("player1.png"),self.file.parse_sprite("player2.png")],
            'right':[self.file.parse_sprite("player3.png"),self.file.parse_sprite("player4.png"),self.file.parse_sprite("player5.png")],
            'left':[pygame.transform.flip(self.file.parse_sprite("player3.png"),True,False),pygame.transform.flip(self.file.parse_sprite("player4.png"),True,False),pygame.transform.flip(self.file.parse_sprite("player5.png"),True,False)],
            'up':[self.file.parse_sprite("player8.png"),self.file.parse_sprite("player9.png"),self.file.parse_sprite("player10.png")],
            'down':[self.file.parse_sprite("player11.png"),self.file.parse_sprite("player12.png")],
            'up_idle':[self.file.parse_sprite("player6.png"),self.file.parse_sprite("player7.png")],
        }

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = "down"
        else:
            self.direction.y = 0
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        elif keys[pygame.K_SPACE]:
            if self.shoot_timer.active == False:
                self.shoot_timer.activate()
                #print(self.shoot_timer.active)
                Bullet((2400,2200),self.group)
        else:
            self.direction.x = 0
     
    def check_lives(self):
        #print(self.lives)
        if self.lives == 0:
            print(self.lives)
            #print("dead")

    def hurt(self):
        if self.hurt_timer.active == False:
            self.health_status = "hurt"
            self.hurt_timer.activate()
            self.lives -= 1

    def animate(self,dt):
        if self.status == "idle":
            self.frame_index += 4 * dt
        else:
            self.frame_index += 8 * dt
        if self.frame_index >=len(self.animations[self.status]):
            self.frame_index = 0
            #print(self.status)

        self.image = self.animations[self.status][int(self.frame_index)]

    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = "idle"
    
    def move(self,dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx 
        self.collision('horizontal')

        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        self.collision('vertical')
        self.enter_room()

    def collision(self,direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite,'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    if direction == "horizontal":
                        if self.direction.x > 0: #moving right
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.x < 0: # moving left
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx
                    
                    if direction == "vertical":
                        if self.direction.y > 0: #moving down
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction.y < 0: # moving up
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery

    def enter_room(self):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite,'enterbox'):
                if sprite.enterbox.colliderect(self.hitbox):
                    if self.location == "overworld":
                        self.temp_pos = self.pos[:] #when copying lists or vectors/arrys a simple assigment wont keep temp var instread var[:]
                        self.pos.x = 6400
                        self.pos.y = 2000
                        self.location = "dungeon"
                    elif self.location == "dungeon":
                        self.pos.x = int(self.temp_pos[0]) + 40
                        self.pos.y = int(self.temp_pos[1]) + 0
                        self.location = "overworld"

    def update(self,dt):
        #print(self.health_status)
        self.input()
        self.get_status()
        self.move(dt)
        if self.hurt_timer.active == True:
            self.hurt_timer.update()
            if self.hurt_timer.active == False:
                self.health_status = "fine"
        self.shoot_timer.update()
        self.check_lives()
        self.animate(dt)