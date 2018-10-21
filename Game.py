import pygame
from menu import Menu
from scoreboard import Scoreboard
from settings import Settings
from eventloop import EventLoop
from os import path

class Game:

    def __init__(self):
        pygame.init()
        self.ai_settings = Settings()
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height))
        pygame.display.set_caption("Super Mario Bros.!")

        self.menu = Menu(self.screen, 'Super Mario Bros', 'TOP - ')
        self.sb = Scoreboard(self.ai_settings, self. screen)
        self.load_data()

    def load_data(self):
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, self.ai_settings.hs_file), 'r') as f:
            try:
                self.ai_settings.high_score = int(f.read())
            except:
                self.ai_settings.high_score = 0

    def play(self):
        eloop = EventLoop(self.ai_settings.finished)
        self.load_data()

        while not eloop.finished:
            eloop.check_events(self.ai_settings, self.menu)
            self.sb.check_high_score(self.sb)
            self.update_screen()

    def update_screen(self):
        self.screen.fill(self.ai_settings.bg_color)

        if not self.ai_settings.finished:
            self.menu.blitme()
            self.sb.check_high_score(self.sb)
            self.sb.prep_high_score()
            self.sb.display_high_score()
            self.menu.draw_menu()

        else:
            self.sb.show_score()

        pygame.display.flip()


game = Game()
game.play()
