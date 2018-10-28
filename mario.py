import pygame
from pygame.sprite import Sprite


class Mario(Sprite):

    def __init__(self, ai_settings, screen):
        super(Mario, self).__init__(ai_settings, screen)
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/mario.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # spawn position ------

        # ---------------------

        self.moving_right = False
        self.moving_left = False
        self.jump = False

    # def update(self):

    def blitme(self):
        self.screen.blit(self.image, self.rect)
