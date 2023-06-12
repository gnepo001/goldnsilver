import pygame

import settings as S
from player import Player
from timer import Timer
from tiles import TileMap
from spritesheet import SpriteSheet

from entity import Enemy

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = CameraGroup()
        self.setup()

    def setup(self):
        self.player = Player((S.SCREEN_WIDTH/2,S.SCREEN_HEIGHT/2),self.all_sprites)
        file = SpriteSheet("tiles.png")
        self.map = TileMap('tile_map.csv',file,groups=self.all_sprites)
        self.enemies = Enemy((50,50),self.all_sprites)

    def run(self,dt):
        self.display_surface.fill('black')
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)

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