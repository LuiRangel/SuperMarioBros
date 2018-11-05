import pygame
from menu import Menu
from scoreboard import Scoreboard
from settings import Settings
from eventloop import EventLoop
from map import Map
from mario import Mario
from os import path
from time import sleep


class Game:

    def __init__(self):
        pygame.init()
        self.ai_settings = Settings()
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height))
        pygame.display.set_caption("Super Mario Bros.")

        self.screen_rect = self.screen.get_rect()
        self.map = Map(self.screen, 'images/world1-1.txt', 'rock_block', 'metal_block', 'stone_block', 'brick_block',
                       'question_block', 'pipe-1')
        self.mario = Mario(self.ai_settings, self.screen, self.map, self)
        self.menu = Menu(self.screen, 'Super Mario Bros', 'TOP - ', 'SCORE', 'COINS', 'TIME', self.ai_settings, self.mario)
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
        eloop = EventLoop(self.ai_settings.finished, self.ai_settings.display_lives)
        self.load_data()

        while not eloop.finished:
            eloop.check_events(self.ai_settings, self.menu, self.mario)
            self.mario.update(self.map.rock, self.map.metal, self.map.stone, self.map.brick, self.map.q)
            self.update_screen()
            self.sb.dec_timer()
            self.sb.check_high_score(self.sb)

    def update_screen(self):
        eloop = EventLoop(self.ai_settings.finished, self.ai_settings.display_lives)
        self.screen.fill(self.ai_settings.bg_color)
        self.sb.prep_high_score()

        if not self.ai_settings.finished:
            self.menu.blitme()
            self.menu.draw_menu()
            self.sb.display_high_score()

        else:
            if eloop.display_lives == True:
                self.menu.prep_lives()
                self.menu.draw_lives()
                self.ai_settings.display_lives = False
                sleep(3)

            self.sb.show_stats()
            self.menu.draw_stats()
            # ==================== check mario pos to see if "scrolling" should occur =================================
            print('pos')
            print(self.mario.pos.x)
            if float(self.mario.pos.x) + float(self.mario.acc.x) >= float(self.ai_settings.screen_half_width) \
                    and self.mario.moving_right:
                diff = float(self.mario.pos.x) - self.ai_settings.screen_half_width
                print('diff')
                print(diff)
                self.mario.pos.x = self.ai_settings.screen_half_width
                # diff = 1
                self.map.shift_level(-diff)
            # elif float(self.mario.pos.x) + float(self.mario.acc.x) <= float(self.screen_half_width)
            # and self.mario.moving_left:
            #     diff = float(self.mario.pos.x) - self.screen_half_width
            #     print('diff')
            #     print(diff)
            #     self.mario.pos.x = self.screen_half_width
            #     diff = -1 + diff
            #     self.map.shift_level(-diff)
            # =========================================================================================================
            self.map.blitme()
            self.mario.blitme()
            if self.mario.death == True:
                self.menu.prep_lives()
                self.menu.draw_lives()
                sleep(3)

        pygame.display.flip()


game = Game()
game.play()