import pygame 
from spritesheet import SpriteSheet

class Entity(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = None
        self.rect = self.image.get_rect(center=pos)
        self.z = None



class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.import_assets()
        self.frame_index = 0
        self.status = "idle"
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.z = 7

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
            print(self.status)

        self.image = self.animations[self.status][int(self.frame_index)]
    
    def move(self,dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = round(self.pos.x)

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = round(self.pos.y)


    def update(self,dt):
        
        #self.move(dt)
        self.animate(dt)
