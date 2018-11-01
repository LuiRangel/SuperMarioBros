import pygame
from menu import Menu
from scoreboard import Scoreboard
from settings import Settings
from eventloop import EventLoop
from map import Map
from mario import Mario
from os import path


class Game:

    def __init__(self):
        pygame.init()
        self.ai_settings = Settings()
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height))
        pygame.display.set_caption("Super Mario Bros.")

        self.screen_rect = self.screen.get_rect()
        self.menu = Menu(self.screen, 'Super Mario Bros', 'TOP - ')
        self.map = Map(self.screen, 'images/world1-1.txt', 'stone_block')
        self.mario = Mario(self.ai_settings, self.screen, self.map, self)
        self.sb = Scoreboard(self.ai_settings, self.screen)
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
            eloop.check_events(self.ai_settings, self.menu, self.mario)
            self.update_screen()
            self.mario.update(self.map.stone)
            self.sb.check_high_score(self.sb)

    def update_screen(self):
        self.screen.fill(self.ai_settings.bg_color)
        self.sb.prep_high_score()

        if not self.ai_settings.finished:
            self.menu.blitme()
            self.menu.draw_menu()
            self.sb.display_high_score()

        else:
            self.sb.show_stats()
            self.map.blitme()
            self.mario.blitme()

        pygame.display.flip()


game = Game()
game.play()