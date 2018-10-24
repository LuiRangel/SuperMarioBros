import pygame.font


class Menu:

    def __init__(self, screen, title, score_menu):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.title_font = pygame.font.SysFont(None, 100)
        self.score_menu_font = pygame.font.SysFont(None, 50)
        self.title_color = (254, 249, 27)
        self.score_menu_color = (255, 255, 255)
        self.title = title
        self.score_menu = score_menu

        self.title_image = False
        self.title_image_rect = False

        self.play_button = Button(screen, 'PLAY')
        self.prep_title(self.title)
        self.prep_score_menu(self.score_menu)

    def prep_title(self, title):
        self.title_image = self.title_font.render(title, True, self.title_color, None)
        self.title_image_rect = self.title_image.get_rect()

        self.title_image_rect.centerx = self.screen_rect.centerx
        self.title_image_rect.centery = self.screen_rect.centery - (self.screen_rect.centery / 2)

    def prep_score_menu(self, score_menu):
        self.score_menu_image = self.score_menu_font.render(score_menu, True, self.score_menu_color, None)
        self.score_menu_image_rect = self.score_menu_image.get_rect()

        self.score_menu_image_rect.centerx = self.screen_rect.centerx - 50
        self.score_menu_image_rect.centery = self.screen_rect.centery - 100

    def draw_menu(self):
        self.screen.blit(self.title_image, self.title_image_rect)
        self.screen.blit(self.score_menu_image, self.score_menu_image_rect)
        self.play_button.draw_button()


class Button:

    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.font_color = (7, 243, 229)

        # build the button's rect and position it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
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