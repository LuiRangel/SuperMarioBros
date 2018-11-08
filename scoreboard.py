import pygame.font
from os import path


class Scoreboard():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 50)

        self.prep_score()
        self.prep_high_score()

    def reset_stats(self):
        self.ai_settings.score = 0
        self.ai_settings.time = 0
        self.ai_settings.time = 0

    def prep_score(self):
        score_str = str(self.ai_settings.score)
        coins_str = str(self.ai_settings.coins)
        time_str = str(self.ai_settings.time)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.coins_image = self.font.render(coins_str, True, self.text_color, self.ai_settings.bg_color)
        self.time_image = self.font.render(time_str, True, self.text_color, self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.left + 100
        self.score_rect.centery = self.screen_rect.top + 60

        self.coins_rect = self.coins_image.get_rect()
        self.coins_rect.centerx = self.screen_rect.width / 2
        self.coins_rect.centery = self.screen_rect.top + 60

        self.time_rect = self.time_image.get_rect()
        self.time_rect.centerx = self.screen_rect.right - 100
        self.time_rect.centery = self.screen_rect.top + 60


    def prep_high_score(self):
        high_score = int(round(self.ai_settings.high_score, -1))
        high_score_str = "{:,}".format(high_score)

        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx + 40
        self.high_score_rect.centery = self.screen_rect.centery + 200

    def dec_timer(self):
        self.ai_settings.time -= 1

    def show_stats(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.coins_image, self.coins_rect)
        self.screen.blit(self.time_image, self.time_rect)

    def display_high_score(self):
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def check_high_score(self, sb):
        if self.ai_settings.score > self.ai_settings.high_score:
            self.ai_settings.high_score = self.ai_settings.score
            self.dir = path.dirname(__file__)
            with open(path.join(self.dir, self.ai_settings.hs_file), 'w') as f:
                f.write(str(self.ai_settings.high_score))
        sb.prep_high_score()