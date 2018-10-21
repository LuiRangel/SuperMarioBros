import pygame
from settings import Settings
from eventloop import EventLoop
from menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.ai_settings = Settings()
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height))
        pygame.display.set_caption("Super Mario Bros.!")

        self.menu = Menu(self.screen)

    def play(self):
        eloop = EventLoop(self.ai_settings.finished)

        while not eloop.finished:
            eloop.check_events(self.ai_settings)
            self.update_screen()

    def update_screen(self):
        self.screen.fill(self.ai_settings.bg_color)

        if not self.ai_settings.finished:
            self.menu.draw_menu()

        pygame.display.flip()


game = Game()
game.play()
