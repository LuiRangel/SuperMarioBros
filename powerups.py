import pygame
from pygame.sprite import Sprite
from time import sleep
vec = pygame.math.Vector2


class Pow(Sprite):
    def __init__(self, ai_settings, screen, map, Game):
        super(Pow, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.map = map
        self.game = Game
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('images/mushroom.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = float(self.screen_rect.width / 2)
        self.rect.centery = float(self.screen_rect.height - 100)
        self.center = float(self.rect.centerx)
        self.vx = 0.5

    def update(self):
        #self.rect.centery = self.screen_rect.height / 2
        self.rect.x += self.vx

    def blitme(self):
        self.screen.blit(self.image, self.rect)