import pygame
from pygame.sprite import Sprite
from time import sleep


class Pacman(Sprite):
    def __init__(self, screen, ai_settings):
        super(Pacman, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.images = []
        self.images.append(pygame.image.load('images/pacmanH-1.png'))
        self.images.append(pygame.image.load('images/pacmanH-2.png'))
        self.images.append(pygame.image.load('images/pacmanV-1.png'))
        self.images.append(pygame.image.load('images/pacmanV-2.png'))

        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.orientation = "Left"

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery - 40

        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        #sleep(0.00001)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.index += 1
            if self.index > 1:
                self.index = 0
            self.image = self.images[self.index]
            self.rect.centerx += self.ai_settings.pacman_speed

        if self.moving_left and self.rect.left > 0:
            self.index += 1
            if self.index > 1:
                self.index = 0
            self.image = self.images[self.index]
            self.rect.centerx -= self.ai_settings.pacman_speed

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.index += 1
            if self.index > 3:
                self.index = 2
            self.image = self.images[self.index]
            self.rect.centery -= self.ai_settings.pacman_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.index += 1
            if self.index > 3:
                self.index = 2
            self.image = self.images[self.index]
            self.rect.centery += self.ai_settings.pacman_speed


    def blitme(self):
        if self.orientation == "Right":
            self.screen.blit(pygame.transform.flip(self.image, True, False), self.rect)
        elif self.orientation == "Left":
            self.screen.blit(self.image, self.rect)
        elif self.orientation == "Up":
            self.screen.blit(self.image, self.rect)
        elif self.orientation == "Down":
            self.screen.blit(pygame.transform.flip(self.image, False, True), self.rect)


    def center_pacman(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery - 40
        #self.center = self.screen_rect.center


    def check_wall_collision(self, bricks):
        for brick in bricks:
            if self.rect.colliderect(brick):
                if self.moving_left and self.rect.left >= brick.centerx:
                    self.rect.left = brick.right + 4
                    return
                elif self.moving_right and self.rect.right <= brick.centerx:
                    self.rect.right = brick.left - 4
                    return
                if self.moving_up and self.rect.top >= brick.centery:
                    self.rect.top = brick.bottom + 4
                    return
                elif self.moving_down and self.rect.bottom <= brick.centery:
                    self.rect.bottom = brick.top - 4
                    return

    def check_dot_collision(self, ai_settings, dots, pills, sb):
        counter = 0
        for dot in dots:
            if self.rect.colliderect(dot):
                del dots[counter]
                self.ai_settings.score += self.ai_settings.dot_points
                sb.prep_score()
            counter += 1
        counter = 0

        for pill in pills:
            if self.rect.colliderect(pill):
                #pygame.mixer.Sound.play(ai_settings.waka)
                del pills[counter]
                self.ai_settings.score += self.ai_settings.pill_points
                sb.prep_score()
            counter += 1