import pygame
from imagerect import ImageRect
from pygame.sprite import Group


class Maze:
    RED = (255, 0, 0)
    # BRICK_SIZE = 13
    BRICK_SIZE = 25
    DOT_SIZE = 10
    PILL_SIZE = 20

    def __init__(self, screen, mazefile, brickfile, dotfile, powerpill):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = []

        self.dots = []
        # self.dots = Group()

        self.pills = []
        sz = Maze.BRICK_SIZE
        sz1 = Maze.DOT_SIZE
        sz2 = Maze.PILL_SIZE

        self.brick = ImageRect(screen, brickfile, sz, sz)

        self.dot = ImageRect(screen, dotfile, sz1, sz1)
        # self.dots.add(ImageRect(screen, dotfile, sz1, sz1))

        self.pill = ImageRect(screen, powerpill, sz2, sz2)
        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.build()

    def __str__(self): return 'maze(' + self.filename + ')'

    def build(self):
        r = self.brick.rect
        d = self.dot.rect
        w, h = r.width, r.height
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'x':
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'o':
                    self.dots.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                    # self.dots.add(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'P':
                    self.pills.append(pygame.Rect(ncol * dx, nrow * dy, w, h))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for rect in self.dots:
            self.screen.blit(self.dot.image, rect)
        for rect in self.pills:
            self.screen.blit(self.pill.image, rect)