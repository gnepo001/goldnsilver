import pygame

from spritesheet import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.import_assets()
        self.frame_index = 0
        self.image = self.idle_frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)


    def import_assets(self):
        self.file = SpriteSheet("sprites.png")

        self.walk_frames = [
            self.file.parse_sprite("player3.png"),
            self.file.parse_sprite("player4.png"),
            self.file.parse_sprite("player5.png"),
            #self.file.parse_sprite("player6.png")
        ]
       
        self.idle_frames = [
            self.file.parse_sprite("player1.png"),
            self.file.parse_sprite("player7.png")
        ]

    def tt(self):
        self.frame_index += 4
        if self.frame_index >=len(self.idle_frames):
            self.frame_index = 0

        self.image = self.walk_frames[int(self.frame_index)]

    def update(self,dt):
        print("called")
        print(self.walk_frames)
        #print(self.frame_index)
        self.frame_index += 8 * dt
        if self.frame_index >=len(self.walk_frames):
            self.frame_index = 0

        self.image = self.walk_frames[int(self.frame_index)]
        