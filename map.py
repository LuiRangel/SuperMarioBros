import pygame
from imagerect import ImageRect


class Map:
    BLOCK_SIZE = 30

    def __init__(self, screen, worldfile, rockfile, metalfile, stonefile, brickfile):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.filename = worldfile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.rock = []
        self.stone = []
        self.metal = []
        self.brick = []
        sz = Map.BLOCK_SIZE

        self.rock_block = ImageRect(screen, rockfile, sz, sz)
        self.stone_block = ImageRect(screen, stonefile, sz, sz)
        self.metal_block = ImageRect(screen, metalfile, sz, sz)
        self.brick_block = ImageRect(screen, brickfile, sz, sz)

        self.deltax = self.deltay = Map.BLOCK_SIZE
        self.spawnx = 0
        self.spawny = 0
        self.map_shift = 0

        self.build()

    def __str__(self): return 'maze(' + self.filename + ')'

    def build(self):
        r = self.rock_block.rect
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
                if col == 'm':
                    self.metal.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == 'r':
                    self.rock.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == 'b':
                    self.brick.append(pygame.Rect(ncol * dx, nrow * dy, w, h))

    # shift blocks depending on mario's relation to the middle of the screen to simulate scrolling
    def shift_level(self, x):
        self.map_shift = x

        for block in self.stone:
            block.x += self.map_shift
        for block in self.metal:
            block.x += self.map_shift
        for block in self.rock:
            block.x += self.map_shift
        for block in self.brick:
            block.x += self.map_shift

    def blitme(self):
        for rect in self.rock:
            if rect.left == self.screen_rect.left:
                del rect
            else:
                self.screen.blit(self.rock_block.image, rect)
        for rect in self.stone:
            if rect.left == self.screen_rect.left:
                del rect
            else:
                self.screen.blit(self.stone_block.image, rect)
        for rect in self.metal:
            if rect.left == self.screen_rect.left:
                del rect
            else:
                self.screen.blit(self.metal_block.image, rect)
        for rect in self.brick:
            if rect.left == self.screen_rect.left:
                del rect
            else:
                self.screen.blit(self.brick_block.image, rect)