import pygame
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
        self.images.append(pygame.image.load('images/mario_jump.png'))
        self.image = self.images[self.index]

        self.image = pygame.transform.scale(self.images[self.index], (50, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.pos = vec(self.map.spawnx, self.map.spawny)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.max_height = 3
        self.height = 0
        self.scroll_vel = vec(0, 0)

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
        self.jump_cut = False
        self.grounded = True

    def update(self, rock, metal, stone, brick, q, p1, p2):
        self.acc = vec(0, self.ai_settings.gravity)

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.acc.x = self.ai_settings.player_acc

            # frame array --------------
            self.index += 1
            if self.index > 2:
                self.index = 1
            self.image = pygame.transform.scale(self.images[self.index], (50, 50))
            # --------------------------

            # deceleration lets mario slide through blocks; collision is detected only when button is held
            if self.rect.collidelist(metal) != -1:
                print('collision')
                self.vel.x = 0
                self.acc.x = 0
                self.pos.x -= 0.01

        if self.moving_left and self.rect.left > 0:
            self.acc.x = -self.ai_settings.player_acc

            # frame array --------------
            self.index += 1
            if self.index > 2:
                self.index = 1
            self.image = pygame.transform.scale(self.images[self.index], (50, 50))
            # --------------------------

            # deceleration lets mario slide through blocks; collision is detected only when button is held
            if self.rect.collidelist(metal) != -1:
                print('collision')
                self.vel.x = 0
                self.acc.x = 0
                #self.pos.x += 0.01

        # -----------------------------------------------------------------------
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.ai_settings.player_speed
            if self.rect.collidelist(rock) != -1:
                self.rect.centery += self.ai_settings.player_speed

        # jump code ================(needs tweaking look at height and flags he's able to jump multiple times)==========
        if self.jump and self.grounded:
            self.grounded = False
            self.jump = False
            self.acc.y -= self.ai_settings.player_jump_acc
            self.height += self.ai_settings.player_jump_acc
            pygame.mixer.Sound.play(self.ai_settings.jump_sound)
            print(self.height)

        if self.height == 0:
            self.jump = False
            self.grounded = False

        if self.jump_cut:
            if self.pos.y < 400:
                self.pos.y = -3

        # ========================================

        # ------------------------------------------------------------------------

        # self.acc.y += self.ai_settings.player_acc
        # if self.rect.collidelist(rock) == -1 and self.rect.bottom < self.screen_rect.bottom:
        #     self.acc.y -= self.ai_settings.player_acc

        if self.vel.y > 0:
            if self.rect.bottom < self.screen_rect.bottom:
                self.rect.centery += self.ai_settings.player_speed
                for block in rock:
                    if self.rect.colliderect(block):
                        self.vel.y = 0
                        self.pos.y = block.top
                        self.height = 0
                        self.grounded = True
                for block in brick:
                    if self.rect.colliderect(block):
                        self.pos.y -= self.vel.y * 1.5
                        self.vel.y = 0
                        self.height = 0
                        self.grounded = True
                for block in q:
                    if self.rect.colliderect(block):
                        self.pos.y -= self.vel.y * 1.5
                        self.vel.y = 0
                        self.height = 0
                        self.grounded = True
                for block in p1:
                    if self.rect.colliderect(block):
                        self.pos.y -= self.vel.y * 1.5
                        self.vel.y = 0
                        self.height = 0
                        self.grounded = True
                for block in p2:
                    if self.rect.colliderect(block):
                        self.pos.y -= self.vel.y * 1.5
                        self.vel.y = 0
                        self.height = 0
                        self.grounded = True

            elif self.rect.bottom == self.screen_rect.bottom:
                self.ai_settings.finished = True

            if self.rect.collidelist(q) != -1:
                self.pos.y -= self.vel.y
                self.vel.y = 0
            if self.rect.collidelist(brick) != -1:
                self.pos.y -= self.vel.y
                self.vel.y = 0
            if self.rect.collidelist(stone) != -1:
                self.pos.y -= self.vel.y
                self.vel.y = 0

        if self.acc.x == 0:
            self.image = pygame.transform.scale(self.images[0], (50, 50))

        # ----------------------final vel/acc/pos----------------------------

        # if self.pos.x <= self.ai_settings.screen_half_width:
        #     self.acc.x += self.vel.x * self.ai_settings.player_friction
        #     self.vel += self.acc
        #     self.pos += self.vel + (0.5 * self.acc)
        # else:
        #     self.acc.x = 0
        #     self.vel.x = 0
        #     self.scroll_vel.x = self.vel.x + self.vel.x * self.ai_settings.player_friction
        #     # self.pos += self.vel + (0.5 * self.acc)

        #  jump acc line
        self.acc.y += self.vel.y * self.ai_settings.player_friction

        self.acc.x += self.vel.x * self.ai_settings.player_friction
        self.vel += self.acc
        self.pos += self.vel + (0.5 * self.acc)

        # detects collision for when button is not pressed/held (sliding mario); but still gets stuck
        # if self.rect.collidelist(metal) != -1:
        #     print('collision')
        #     # sliding left
        #     if self.acc.x < 0:
        #         self.pos += self.vel + (0.5 * self.acc)
        #         self.vel.x = 0
        #         self.acc.x = 0
        #     # sliding right
        #     elif self.acc.x > 0:
        #         self.pos -= self.vel + (0.5 * self.acc)
        #         self.vel.x = 0
        #         self.acc.x = 0

        # update rect using pos
        self.rect.midbottom = self.pos

    def blitme(self):
        # make frames work right for when jumping in the air and landing ============================================
        if self.orientation == "Left":
            self.screen.blit(pygame.transform.flip(self.image, True, False), self.rect)
        elif self.orientation == "Right":
            self.screen.blit(self.image, self.rect)
        # got rid of up orientation statement and replaced it with height check needs work ====================
        elif self.orientation == "Jump":
            pygame.transform.scale(self.images[3], (50, 50))
            self.screen.blit(pygame.transform.scale(self.images[3], (50, 50)), self.rect)
        # =====================================================================================================
        elif self.orientation == "Down":
            self.screen.blit(self.image, self.rect)