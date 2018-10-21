import pygame.font


class Menu:

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.title_image = pygame.image.load('images/Super_Mario_Bros_Logo.png')
        self.title_image_rect = self.title_image.get_rect()

        self.title_image_rect.centerx = self.screen_rect.centerx
        self.title_image_rect.centery = self.screen_rect.centery - (self.screen_rect.centery / 2)

        self.play_button = Button(screen, 'Play Game')

    def draw_menu(self):
        self.screen.blit(self.title_image, self.title_image_rect)
        self.play_button.draw_button()


class Button:

    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.font_color = (230, 230, 230)

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
