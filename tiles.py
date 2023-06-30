import pygame, csv, os

class Tile(pygame.sprite.Sprite):
    def __init__(self,image=None,x=0,y=0,spritesheet=None,groups=None,z=0):
        super().__init__(groups)
        self.image = spritesheet.parse_sprite(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x,y
        self.z = z
       
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x,self.rect.y))

class Barrier(Tile):
    def __init__(self,image,x,y,spritesheet,groups,colli,z):
        super().__init__(image,x,y,spritesheet,groups=[groups,colli],z=z)
        self.hitbox = self.rect.copy().inflate(5,2)

class Stone(Tile):
    def __init__(self,image,x,y,spritesheet,groups,colli,z):
        super().__init__(image,x,y,spritesheet,groups=[groups,colli],z=z)
        self.hitbox = self.rect.copy().inflate(5,2)

class Stairs(Tile):
    def __init__(self,image,x,y,spritesheet,groups,colli,z):
        super().__init__(image,x,y,spritesheet,groups=[groups,colli],z=z)
        self.enterbox = self.rect.copy().inflate(5,2)

class TileMap():
    #takes in file name and spritesheet data, group of tiles
    def __init__(self, filename, spritesheet,groups,colli):
        self.tile_size = 96
        self.current_shift_x = 0
        self.shift_map = False
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        #load in tiles
        #self.tiles = self.load_tiles(filename,groups)
        self.tiles = self.load_tiles(filename,groups,colli)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def draw_map(self, surface):
        surface.blit(self.map_surface, (self.current_shift_x, 0))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map

    def load_tiles(self, filename,groups,colli):
        tiles = []
        map = self.read_csv(filename)
        x, y = 0, 0
        for row in map:
            x = 0
            for tile in row:
                if tile == '0':
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                elif tile == '1':
                    tiles.append(Tile('brown.png', x * self.tile_size, y * self.tile_size, self.spritesheet,groups, z=1))
                elif tile == '2':
                    tiles.append(Tile('green.png', x * self.tile_size, y * self.tile_size, self.spritesheet,groups, z=1))
                elif tile == '3':
                    tiles.append(Stone('stone.png', x * self.tile_size, y * self.tile_size, self.spritesheet,groups,colli, z=1))
                elif tile == '4':
                    tiles.append(Stairs('brown_stairs.png', x * self.tile_size, y * self.tile_size, self.spritesheet,groups,colli, z=1))
                elif tile == '5':
                    tiles.append(Tile('water.png', x * self.tile_size, y * self.tile_size, self.spritesheet,groups, z=1))
                elif tile == '6':
                    tiles.append(Barrier('water.png', x * self.tile_size, y * self.tile_size, self.spritesheet,groups,colli, z=1))
                elif tile == '7':
                    tiles.append(Barrier('stone_greenTop.png', x * self.tile_size, y * self.tile_size, self.spritesheet,groups,colli, z=1))
                elif tile == '8':
                    tiles.append(Barrier('tree.png', x * self.tile_size, y * self.tile_size, self.spritesheet,groups,colli, z=1))
                elif tile == '9':
                    tiles.append(Barrier('tree_2.png', x * self.tile_size, y * self.tile_size, self.spritesheet,groups,colli, z=1))
                elif tile == '10':
                    tiles.append(Tile('purple_stone.png', x * self.tile_size, y * self.tile_size, self.spritesheet,groups, z=1))
                elif tile == '11':
                    tiles.append(Stone('purple_brick.png', x * self.tile_size, y * self.tile_size, self.spritesheet,groups,colli, z=1))
                    # Move to next tile in current row
                x += 1

            # Move to next row
            y += 1
            # Store the size of the tile map
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles

