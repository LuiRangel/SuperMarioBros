import pygame
from pygame.sprite import Sprite
from time import sleep
vec = pygame.math.Vector2


class Mobs(Sprite):

    def __init__(self, ai_settings, screen, map, Game):
        super(Mobs, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.map = map
        self.game = Game
        self.screen_rect = screen.get_rect()

        self.pos = vec(self.map.spawnx, self.map.spawny)
        self.g_vel = vec(0, 0)
        self.k_vel = vec(0, 0)
        self.current_frame = 0
        self.last_update = 0
        self.load_images()

        self.g_image = self.g_walk_frames_r[0]
        self.k_image = self.k_walk_frames_r[0]

        self.g_rect = self.g_image.get_rect()
        self.g_rect.centerx = self.map.g_spawnx
        self.g_rect.centery = self.map.g_spawny - 100
        self.g_center = float(self.g_rect.centerx)
        self.g_vx = 0.5
        if self.g_rect.right == self.screen_rect.width:
            self.g_vx *= -1
        self.vy = 0

        self.k_rect = self.k_image.get_rect()
        self.k_rect.centerx = self.map.k_spawnx
        self.k_rect.centery = self.map.k_spawny
        self.k_center = float(self.k_rect.centerx)
        self.k_vx = 1

    def load_images(self):
        self.g_walk_frames_r = [pygame.image.load('images/goomba.png'),
                                pygame.transform.flip(pygame.image.load('images/goomba.png'), True, False)]

        self.k_walk_frames_r = [pygame.image.load('images/koopa.png'),
                                pygame.image.load('images/koopa-2.png')]
        self.k_walk_frames_l = []
        for frame in self.k_walk_frames_r:
            self.k_walk_frames_l.append(pygame.transform.flip(frame, True, False))


    def g_animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.g_walk_frames_r)
            bottom = self.g_rect.bottom
            if self.g_vel.x > 0:
                self.g_image = self.g_walk_frames_r[self.current_frame]
            # else:
            #     self.g_image = self.g_walk_frames_l[self.current_frame]
            self.g_rect = self.g_image.get_rect()
            self.g_rect.bottom = bottom

    def k_animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 1000:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.k_walk_frames_r)
            bottom = self.k_rect.bottom
            if self.k_vel.x > 0:
                self.k_image = self.k_walk_frames_r[self.current_frame]
            else:
                self.k_image = self.k_walk_frames_l[self.current_frame]
            self.k_rect = self.k_image.get_rect()
            self.k_rect.bottom = bottom

    def update(self):
        # print('spawn x:', self.map.k_spawnx)
        # print('spawn y:', self.map.k_spawny)
        self.g_rect.x += self.g_vx
        self.k_rect.x += self.k_vx
        self.g_animate()
        self.k_animate()


    def blitme(self):
        self.screen.blit(self.g_image, self.g_rect)
        self.screen.blit(self.k_image, self.k_rect)