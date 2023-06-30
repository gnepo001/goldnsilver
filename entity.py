import pygame 
from spritesheet import SpriteSheet

class Entity(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = None
        self.rect = self.image.get_rect(center=pos)
        self.z = None
        

class Key(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.import_assets()
        self.frame_index = 0
        self.image = self.animations[self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.z = 7

    def import_assets(self):
        self.file = SpriteSheet("sprites.png")
        self.animations = [self.file.parse_sprite("key1.png"),self.file.parse_sprite("key2.png")]
        

    def animate(self,dt):
        self.frame_index += 6 * dt
        if self.frame_index >=len(self.animations):
            self.frame_index = 0
        self.image = self.animations[int(self.frame_index)]

    def update(self,dt):
        self.animate(dt)

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,group,player):
        super().__init__(group)
        self.import_assets()
        self.frame_index = 0
        self.status = "idle"
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.z = 7
        self.player = player
        self.dir = False
       

        self.direction = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        self.pos = pygame.math.Vector2(self.rect.center)
    
    def import_assets(self):
        self.file = SpriteSheet('sprites.png')
        self.animations = {
            'idle':[self.file.parse_sprite("enemy1.png"),self.file.parse_sprite("enemy2.png")],
            'right':[self.file.parse_sprite("enemy3.png"),self.file.parse_sprite("enemy4.png"),self.file.parse_sprite("enemy5.png")],
            'left':[pygame.transform.flip(self.file.parse_sprite("enemy3.png"),True,False),pygame.transform.flip(self.file.parse_sprite("enemy4.png"),True,False),pygame.transform.flip(self.file.parse_sprite("enemy5.png"),True,False)],
            'up':[self.file.parse_sprite("enemy8.png"),self.file.parse_sprite("enemy9.png"),self.file.parse_sprite("enemy10.png")],
            'down':[self.file.parse_sprite("enemy11.png"),self.file.parse_sprite("enemy12.png")],
            'up_idle':[self.file.parse_sprite("enemy6.png"),self.file.parse_sprite("enemy7.png")],
        }

    def animate(self,dt):
        if self.status == "idle":
            self.frame_index += 4 * dt
        else:
            self.frame_index += 8 * dt
        if self.frame_index >=len(self.animations[self.status]):
            self.frame_index = 0
            #print(self.status)

        self.image = self.animations[self.status][int(self.frame_index)]
    
    def move(self,dt):
        if self.dir == False and self.pos.x <= 300:
            if self.pos.x <= 300:
                self.pos.x += 1 * self.speed * dt
                self.rect.centerx = round(self.pos.x)
        else:
            self.pos.x -= 1 * self.speed * dt
            self.rect.centerx = round(self.pos.x)

        self.rect.centery = round(self.pos.y)

    def patrol(self,player):
        #if player.pos.x and player.pos.y <= (self.pos.x+100) and (self.pos.y+100):
        #    print("inrange")
        if player.pos.x <= (self.pos.x+300):
            if player.pos.y <= self.pos.y+300:
                pass
                #print("inrange")
                #print('fire')

    def update(self,dt):
        
        #self.move(dt)
        self.patrol(self.player)
        self.animate(dt)
