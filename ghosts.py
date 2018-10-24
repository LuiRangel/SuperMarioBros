import pygame
from pygame.sprite import Sprite

class Pinky(Sprite):
    def __init__(self, screen, ai_settings):
        super(Pinky, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        self.images = []
        self.images.append(pygame.image.load('images/pinkyH-1.png'))
        self.images.append(pygame.image.load('images/pinkyH-2.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        #self.rect.x = self.rect.width
        #self.rect.y = self.rect.height
        self.rect.centerx = self.screen_rect.width / 2
        self.rect.centery = (self.screen_rect.centery / 2) + 60
        self.x = float(self.rect.x)

    def check_wall_collision(self, bricks):
        for brick in bricks:
            if self.rect.colliderect(brick):
                if self.rect.left >= brick.centerx:
                    self.ai_settings.pinky_direction *= -1
                    return
                elif self.rect.right <= brick.centerx:
                    self.ai_settings.pinky_direction *= -1
                    return
                if self.rect.top >= brick.centery:
                    self.ai_settings.pinky_direction *= -1
                    return
                elif self.rect.bottom <= brick.centery:
                    self.ai_settings.pinky_direction *= -1
                    return

    def update(self):
        self.x += (self.ai_settings.ghost_speed * self.ai_settings.pinky_direction)
        self.rect.x = self.x

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Blinky(Sprite):
    def __init__(self, screen, ai_settings):
        super(Blinky, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        self.images = []
        self.images.append(pygame.image.load('images/blinkyH-1.png'))
        self.images.append(pygame.image.load('images/blinkyH-2.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = (self.rect.height / 4) + 30
        #self.rect.centerx = self.screen_rect.centerx
        #self.rect.centery = self.screen_rect.centery
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_wall_collision(self, bricks):
        for brick in bricks:
            if self.rect.colliderect(brick):
                if self.rect.left >= brick.centerx:
                    self.ai_settings.blinky_direction *= -1
                    return
                elif self.rect.right <= brick.centerx:
                    self.ai_settings.blinky_direction *= -1
                    return
                if self.rect.top >= brick.centery:
                    self.ai_settings.blinky_direction *= -1
                    return
                elif self.rect.bottom <= brick.centery:
                    self.ai_settings.blinky_direction *= -1
                    return

    def update(self):
        self.y += (self.ai_settings.ghost_speed * self.ai_settings.blinky_direction)
        self.rect.x = self.x
        self.rect.y = self.y

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Inky(Sprite):
    def __init__(self, screen, ai_settings):
        super(Inky, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        self.images = []
        self.images.append(pygame.image.load('images/inkyH-1.png'))
        self.images.append(pygame.image.load('images/inkyH-2.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.rect.x = (self.screen_rect.width * 0.75) - 30
        self.rect.y = (self.rect.height / 2) + 20
        #self.rect.centerx = self.screen_rect.centerx
        #self.rect.centery = self.screen_rect.centery
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_wall_collision(self, bricks):
        for brick in bricks:
            if self.rect.colliderect(brick):
                if self.rect.left >= brick.centerx:
                    self.ai_settings.inky_direction *= -1
                    return
                elif self.rect.right <= brick.centerx:
                    self.ai_settings.inky_direction *= -1
                    return
                if self.rect.top >= brick.centery:
                    self.ai_settings.inky_direction *= -1
                    return
                elif self.rect.bottom <= brick.centery:
                    self.ai_settings.inky_direction *= -1
                    return

    def update(self):
        self.y += (self.ai_settings.ghost_speed * self.ai_settings.inky_direction)
        self.rect.x = self.x
        self.rect.y = self.y

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Clyde(Sprite):
    def __init__(self, screen, ai_settings):
        super(Clyde, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        self.images = []
        self.images.append(pygame.image.load('images/clydeH-1.png'))
        self.images.append(pygame.image.load('images/clydeH-2.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = (self.screen_rect.height) / 8
        #self.rect.centerx = self.screen_rect.centerx
        #self.rect.centery = self.screen_rect.centery
        self.x = float(self.rect.x)

    def check_wall_collision(self, bricks):
        for brick in bricks:
            if self.rect.colliderect(brick):
                if self.rect.left >= brick.centerx:
                    self.ai_settings.clyde_direction *= -1
                    return
                elif self.rect.right <= brick.centerx:
                    self.ai_settings.clyde_direction *= -1
                    return
                if self.rect.top >= brick.centery:
                    self.ai_settings.clyde_direction *= -1
                    return
                elif self.rect.bottom <= brick.centery:
                    self.ai_settings.clyde_direction *= -1
                    return

    def update(self):
        self.x += (self.ai_settings.ghost_speed * self.ai_settings.clyde_direction)
        self.rect.x = self.x

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def blitme(self):
        self.screen.blit(self.image, self.rect)