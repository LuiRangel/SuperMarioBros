import pygame
from settings import Settings
from pygame.sprite import Sprite
vec = pygame.math.Vector2

class Mario(Sprite):

    def __init__(self, ai_settings, screen, map, Game):
        super(Mario, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.map = map
        self.game = Game
        self.screen_rect = screen.get_rect()
        self.orientation = "Right"

        self.images = []
        self.index = 0
        self.images.append(pygame.image.load('images/mario.png'))
        self.images.append(pygame.image.load('images/mario_run-1.png'))
        self.images.append(pygame.image.load('images/mario_run-2.png'))
        self.image = self.images[self.index]

        #self.image = pygame.image.load('images/mario.png')
        self.image = pygame.transform.scale(self.images[self.index], (50, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.pos = vec(self.map.spawnx, self.map.spawny)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        # spawn position ------
        self.rect.centerx = self.map.spawnx
        self.rect.centery = self.map.spawny
        self.center = float(self.rect.centerx)
        # ---------------------

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.jump = False

    def jump(self, stone):
        self.rect.x += 1
        hits = self.rect.collidelist(stone)     #self.rect.colliderect(block)
        self.rect.x -= 1

        if hits:
            self.vel.y = -20

    def update(self, stone):
        self.acc = vec(0, self.ai_settings.gravity)

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.acc.x = self.ai_settings.player_acc
            self.index += 1
            if self.index > 2:
                self.index = 1
            self.image = pygame.transform.scale(self.images[self.index], (50, 50))
            if self.rect.collidelist(stone) != -1:
                self.rect.centerx -= self.ai_settings.player_speed

        if self.moving_left and self.rect.left > 0:
            self.acc.x = -self.ai_settings.player_acc
            self.index += 1
            if self.index > 2:
                self.index = 1
            self.image = pygame.transform.scale(self.images[self.index], (50, 50))
            if self.rect.collidelist(stone) != -1:
                self.rect.centerx += self.ai_settings.player_speed

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.ai_settings.player_speed
            if self.rect.collidelist(stone) != -1:
                self.rect.centery += self.ai_settings.player_speed

<<<<<<< HEAD
        self.acc.y += self.ai_settings.player_acc
        if self.rect.collidelist(stone) == -1 and self.rect.bottom < self.screen_rect.bottom:
            self.acc.y -= self.ai_settings.player_acc

        # if self.rect.bottom < self.screen_rect.bottom:
        #     self.rect.centery += self.ai_settings.player_speed
        #     if self.rect.collidelist(stone) != -1:
        #         self.rect.centery -= self.ai_settings.player_speed * self.acc.y
        #         print('collision')
=======
        if self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ai_settings.player_speed
            for block in stone:
                if self.rect.colliderect(block):
                    self.vel.y = 0
                    self.pos.y = block.top

        if self.vel.x == 0:
            self.image = pygame.transform.scale(self.images[0], (50, 50))

>>>>>>> refs/remotes/origin/alex-garcia12-physics-patch-2

        self.acc.x += self.vel.x * self.ai_settings.player_friction
        self.vel += self.acc
        self.pos += self.vel + (0.5 * self.acc)
        self.rect.midbottom = self.pos

    def blitme(self):
        if self.orientation == "Left":
            self.screen.blit(pygame.transform.flip(self.image, True, False), self.rect)
        elif self.orientation == "Right":
            self.screen.blit(self.image, self.rect)
        elif self.orientation == "Up":
            self.screen.blit(self.image, self.rect)
        elif self.orientation == "Down":
            self.screen.blit(self.image, self.rect)