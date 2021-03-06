import pygame as pg
import sys
from settings import *

class Game():
    def __init__(self):
        
        # general setup
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGTH))
        self.clock = pg.time.clock()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            self.screen.fill('black')
            pg.display.update()
            self.clock.tick(FPS)




if __name__ == '__main__':
    game = Game()
    game.run()