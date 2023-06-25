import pygame

from spritesheet import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group,collision_sprites):
        super().__init__(group)
        self.import_assets()
        self.frame_index = 0
        self.status = "idle"
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.z = 7
        self.collision_sprites = collision_sprites
        

        #movement
        self.direction = pygame.math.Vector2(self.rect.center)
        self.speed = 300
        self.pos = pygame.math.Vector2(self.rect.center)

        #collison
        #self.hitbox = self.rect.copy().inflate((-126,-70))
        self.hitbox = self.rect.copy().inflate((-30,-30))

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
        else:
            self.direction.x = 0
     
           

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



    def update(self,dt):
        self.input()
        self.get_status()
        self.move(dt)
        self.animate(dt)