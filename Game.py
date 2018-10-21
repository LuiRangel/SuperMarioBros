import pygame
from menu import Menu
from scoreboard import Scoreboard
from settings import Settings
from eventloop import EventLoop


class Game:

    def __init__(self):
        pygame.init()
        self.ai_settings = Settings()
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height))
        pygame.display.set_caption("Super Mario Bros.!")

        self.menu = Menu(self.screen, 'Super Mario Bros', 'HIGH SCORE:')
        self.sb = Scoreboard(self.ai_settings, self. screen)


    def play(self):
        eloop = EventLoop(self.ai_settings.finished)

        while not eloop.finished:
            eloop.check_events(self.ai_settings, self.menu)
            self.update_screen()
            self.sb.check_high_score(self.sb)

    def update_screen(self):
        self.screen.fill(self.ai_settings.bg_color)
        self.sb.prep_high_score()

        if not self.ai_settings.finished:
            self.menu.draw_menu()
            self.menu.blitme()

        pygame.display.flip()


game = Game()
game.play()
