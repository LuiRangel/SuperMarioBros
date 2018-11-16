import pygame
from imagerect import ImageRect


class Map:
    BLOCK_SIZE = 48

    def __init__(self, screen, worldfile, rockfile, metalfile, stonefile, brickfile, quesfile, pipefile, pipefile_1, coinfile,  polefile, flagfile, topfile, castlefile):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.filename = worldfile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.rock = []
        self.stone = []
        self.metal = []
        self.brick = []
        self.q = []
        self.pipe = []
        self.pipe_1 = []
        self.coins = []
        self.pole = []
        self.flags = []
        self.tops = []
        self.castle = []
        sz = Map.BLOCK_SIZE

        self.rock_block = ImageRect(screen, rockfile, sz, sz)
        self.stone_block = ImageRect(screen, stonefile, sz, sz)
        self.metal_block = ImageRect(screen, metalfile, sz, sz)
        self.brick_block = ImageRect(screen, brickfile, sz, sz)
        self.q_block = ImageRect(screen, quesfile, sz, sz)
        self.pipe_block = ImageRect(screen, pipefile, sz, sz)
        self.long_pipe = ImageRect(screen, pipefile_1, sz, sz)
        self.coin = ImageRect(screen, coinfile, sz, sz)
        self.pole_block = ImageRect(screen, polefile, sz, sz)
        self.flag = ImageRect(screen, flagfile, sz, sz)
        self.top = ImageRect(screen, topfile, sz, sz)
        self.cas = ImageRect(screen, castlefile, sz, sz)

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
                if col == 'q':
                    self.q.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == 'P':
                    self.pipe.append(pygame.Rect(ncol * dx, nrow * dy - 28, self.pipe_block.rect.width, self.pipe_block.rect.height + 100))
                if col == 'p':
                    self.pipe_1.append(pygame.Rect(ncol * dx, nrow * dy - 28, self.long_pipe.rect.width,
                                                   self.long_pipe.rect.height))
                if col == 'c':
                    self.coins.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == '|':
                    self.pole.append(pygame.Rect(ncol * dx, nrow * dy, self.pole_block.rect.width,
                                                 self.pole_block.rect.height))
                if col == '>':
                    self.flags.append(pygame.Rect(ncol * dx, nrow * dy, self.flag.rect.width,
                                                  self.flag.rect.height))
                if col == 'o':
                    self.tops.append(pygame.Rect(ncol * dx, nrow * dy, self.top.rect.width, self.top.rect.height))
                if col == 'C':
                    self.castle.append(pygame.Rect(ncol * dx, nrow * dy, self.cas.rect.width, self.cas.rect.height))

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
        for block in self.q:
            block.x += self.map_shift
        for block in self.pipe:
            block.x += self.map_shift
        for block in self.pipe_1:
            block.x += self.map_shift
        for block in self.coins:
            block.x += self.map_shift
        for block in self.pole:
            block.x += self.map_shift
        for block in self.flags:
            block.x += self.map_shift
        for block in self.tops:
            block.x += self.map_shift
        for block in self.castle:
            block.x += self.map_shift

    def blitme(self):
        for rect in self.rock:
            if rect.right == self.screen_rect.left:
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
        for rect in self.q:
            if rect.left == self.screen_rect.left:
                del rect
            else:
                self.screen.blit(self.q_block.image, rect)
        for rect in self.pipe:
            if rect.left == self.screen_rect.left:
                del rect
            else:
                self.screen.blit(pygame.transform.scale(self.pipe_block.image, (75, 75)), rect)
        for rect in self.pipe_1:
            if rect.left == self.screen_rect.left:
                del rect
            else:
                self.screen.blit(pygame.transform.scale(self.long_pipe.image, (75, 75)), rect)
        for rect in self.coins:
            if rect.left == self.screen_rect.left:
                del rect
            else:
                # self.pipe_block.image = pygame.transform.scale(self.pipe_block.image, (50, 50))
                self.screen.blit(pygame.transform.scale(self.coin.image, (75, 75)), rect)
        for rect in self.pole:
            if rect.left == self.screen_rect.left:
                del rect
            else:
                self.screen.blit(self.pole_block.image, rect)
        for rect in self.flags:
            if rect.left == self.screen_rect.left:
                del rect
            else:
                self.screen.blit(self.flag.image, rect)
        for rect in self.tops:
            if rect.left == self.screen_rect.left:
                del rect
            else:
                self.screen.blit(self.top.image, rect)
        for rect in self.castle:
            if rect.left == self.screen_rect.left:
                del rect
            else:
                self.screen.blit(self.cas.image, rect)