import pygame

import settings as S
from player import Player
from timer import Timer
from tiles import TileMap
from spritesheet import SpriteSheet

from entity import Enemy,Key,Ghost
from bullet import Bullet

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group() #need to create a list of entites to keep track of it
        self.setup()

    def setup(self):
        #self.player = Player((S.SCREEN_WIDTH/2,S.SCREEN_HEIGHT/2),self.all_sprites)
        file = SpriteSheet("tiles.png")
        self.map = TileMap('tile_map.csv',file,groups=self.all_sprites,colli=self.collision_sprites)
        self.player = Player(
            pos=(2800,2700),
            #pos=(6400,2000),
            group=self.all_sprites,
            collision_sprites=self.collision_sprites
            )
        self.enemies = Enemy((2400,1800),self.all_sprites,self.player)
        Enemy((2800,800),self.all_sprites,self.player)
        Enemy((1950,2000),self.all_sprites,self.player)
        Enemy((1500,2200),self.all_sprites,self.player)
        Enemy((920,1000),self.all_sprites,self.player)

        self.key = Key((2400,2400),self.all_sprites)
        self.ghost = Ghost((2500,2400),self.all_sprites,64,150,self.player)
        self.ghost = Ghost((2500,2400),self.all_sprites,64,150,self.player)
        Ghost((2500,1500),self.all_sprites,64,150,self.player)
        Ghost((2500,1700),self.all_sprites,64,150,self.player)
        Ghost((2500,1900),self.all_sprites,64,150,self.player)
        Ghost((2500,2100),self.all_sprites,64,150,self.player)
        Ghost((2500,2600),self.all_sprites,64,150,self.player)
        Ghost((2000,620),self.all_sprites,320,200,self.player)
        Ghost((2000,620),self.all_sprites,320,250,self.player)

        #upper half
        Ghost((750,425),self.all_sprites,800,250,self.player)
        #dungeon 1 ghosts
        Ghost((6355,2050),self.all_sprites,560,150,self.player)
        Ghost((6355,2250),self.all_sprites,560,150,self.player)
        #self.bullet1 = Bullet((2400,2200),self.all_sprites,self.player)
   
    def run(self,dt):
        self.display_surface.fill('black')
        self.all_sprites.custom_draw(self.player)
        #image = SpriteSheet("sprites.png").parse_sprite("heart.png")
        #rect = image.get_rect(center=(50,50))
        self.draw_hud(self.player,self.display_surface)
        self.all_sprites.update(dt)

    def draw_hud(self,player,surf):
        image = SpriteSheet("sprites.png").parse_sprite("heart.png")
        x = 10
        for life in range(0,player.lives):
            surf.blit(image,(x,0))
            x += 100

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - S.SCREEN_WIDTH /2
        self.offset.y = player.rect.centery - S.SCREEN_HEIGHT /2

        #looks through each sprite z levels and draws them according to level
        for layer in S.LAYERS.values():
            for sprite in sorted(self.sprites(),key=lambda sprite:sprite.rect.centery):
                if sprite.z == layer:
           
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)