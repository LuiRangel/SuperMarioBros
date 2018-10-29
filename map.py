import pygame
from imagerect import ImageRect


class Map:
    BLOCK_SIZE = 30

    def __init__(self, screen, worldfile, stonefile):
        self.screen = screen
        self.filename = worldfile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.stone = []
        sz = Map.BLOCK_SIZE

        self.stone_block = ImageRect(screen, stonefile, sz, sz)

        self.deltax = self.deltay = Map.BLOCK_SIZE
        self.spawnx = 0
        self.spawny = 0

        self.build()

    def __str__(self): return 'maze(' + self.filename + ')'

    def build(self):
        r = self.stone_block.rect
        w, h = r.width, r.height
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 's':
                    self.stone.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == 'M':
                    self.spawnx = ncol * dx
                    self.spawny = nrow * dy

    def blitme(self):
        for rect in self.stone:
            self.screen.blit(self.stone_block.image, rect)
