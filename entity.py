import pygame 

class Entity(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group):
        self.image = none
        self.rect = self.image.get_rect(center=pos)
        self.z = 7

class Enemy(Entity):
    def __init__(self,pos,group):
        super().__init__(pos,group):
    
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
