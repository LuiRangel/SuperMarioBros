import pygame.font


class Menu():

    def __init__(self, screen, title, score_menu, current_score, coin_count, timer, ai_settings, mario):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 50)

        self.title_font = pygame.font.SysFont(None, 70)
        self.title_color = (254, 249, 27)
        self.title = title

        self.score_menu_font = pygame.font.SysFont(None, 50)
        self.score_menu_color = (255, 255, 255)
        self.score_menu = score_menu

        self.current_score_font = pygame.font.SysFont(None, 50)
        self.current_score_color = (255, 255, 255)
        self.current_score = current_score

        self.coin_count_font = pygame.font.SysFont(None, 50)
        self.coin_count_color = (255, 255, 255)
        self.coin_count = coin_count

        self.timer_font = pygame.font.SysFont(None, 50)
        self.timer_color = (255, 255, 255)
        self.timer = timer

        self.image = pygame.image.load('images/logo.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx

        self.title_image = False
        self.title_image_rect = False

        self.play_button = Button(screen, '1 Player Game')
        self.prep_title(self.title)
        self.prep_score_menu(self.score_menu)
        self.prep_current_stats(self.current_score, self.coin_count, self.timer)

        if mario.death == True:
            self.prep_lives()
            self.draw_lives()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.play_button.draw_button()

    def prep_title(self, title):
        self.title_image = self.title_font.render(title, True, self.title_color, None)
        self.title_image_rect = self.title_image.get_rect()

        self.title_image_rect.centerx = self.screen_rect.centerx
        self.title_image_rect.centery = self.screen_rect.centery - (self.screen_rect.centery / 2)

    def prep_score_menu(self, score_menu):
        self.score_menu_image = self.score_menu_font.render(score_menu, True, self.score_menu_color, None)
        self.score_menu_image_rect = self.score_menu_image.get_rect()

        self.score_menu_image_rect.centerx = self.screen_rect.centerx - 60
        self.score_menu_image_rect.centery = self.screen_rect.centery + 200

    def prep_current_stats(self, current_score, coin_count, timer):
        self.current_score_image = self.current_score_font.render(current_score, True, self.current_score_color, None)
        self.current_score_image_rect = self.current_score_image.get_rect()
        self.current_score_image_rect.centerx = self.screen_rect.left + 105
        self.current_score_image_rect.centery = self.screen_rect.top + 30

        self.coin_count_image = self.coin_count_font.render(coin_count, True, self.coin_count_color, None)
        self.coin_count_image_rect = self.current_score_image.get_rect()
        self.coin_count_image_rect.centerx = self.screen_rect.centerx + 5
        self.coin_count_image_rect.centery = self.screen_rect.top + 30

        self.timer_image = self.timer_font.render(timer, True, self.timer_color, None)
        self.timer_image_rect = self.timer_image.get_rect()
        self.timer_image_rect.centerx = self.screen_rect.right - 102
        self.timer_image_rect.centery = self.screen_rect.top + 30

    def prep_lives(self):
        lives_str = str(self.ai_settings.mario_lives)
        self.lives_image = self.font.render(lives_str, True, self.WHITE, self.BLACK)

        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.centerx = self.screen_rect.centerx
        self.lives_rect.centery = self.screen_rect.centery

    def draw_menu(self):
        self.screen.blit(self.score_menu_image, self.score_menu_image_rect)

    def draw_stats(self):
        self.screen.blit(self.current_score_image, self.current_score_image_rect)
        self.screen.blit(self.coin_count_image, self.coin_count_image_rect)
        self.screen.blit(self.timer_image, self.timer_image_rect)

    def draw_lives(self):
        self.screen.fill(self.BLACK)
        self.screen.blit(self.lives_image, self.lives_rect)

class Button:

    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (33, 150, 243)
        self.font = pygame.font.SysFont(None, 48)
        self.font_color = (255, 255, 255)

        # build the button's rect and position it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + 150

        self.msg_image = False
        self.msg_image_rect = False

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.font_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.rect.centerx
        self.msg_image_rect.centery = self.rect.centery

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class ScoreButton:

    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.font_color = (7, 243, 229)

        # build the button's rect and position it
        self.rect = pygame.Rect(0, 0, self.width / 2, self.height)
        self.rect.center = self.screen_rect.center

        self.msg_image = False
        self.msg_image_rect = False

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.font_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)