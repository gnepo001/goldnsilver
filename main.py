import pygame, sys
from level import Level

import settings as S

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((S.SCREEN_WIDTH,S.SCREEN_HEIGHT))

        self.level = Level()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            dt = self.clock.tick(60)/1000
            self.level.run(dt)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()

