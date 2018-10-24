import pygame
from maze import Maze
from pacman import Pacman
from ghosts import Pinky
from ghosts import Inky
from ghosts import Blinky
from ghosts import Clyde
from settings import Settings
from eventloop import EventLoop
from scoreboard import Scoreboard
from menu import Menu
from pygame import mixer
from pygame.sprite import Group
from os import path


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        mixer.init()
        ai_settings = Settings()
        self.ai_settings = ai_settings
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height))
        pygame.display.set_caption("Pacman Portal")

        self.menu = Menu(self.screen, 'Pacman  Portal', 'HIGH SCORE:')
        self.maze = Maze(self.screen, 'images/maze.txt', 'brick', 'dot', 'powerpill')
        self.pacman = Pacman(self.screen, self.ai_settings)
        self.pinky = Pinky(self.screen, self.ai_settings)
        self.inky = Inky(self.screen, self.ai_settings)
        self.blinky = Blinky(self.screen, self.ai_settings)
        self.clyde = Clyde(self.screen, self.ai_settings)
        self.sb = Scoreboard(self.ai_settings, self.screen)
        self.load_data()
        self.ghosts = Group()
        self.ghosts.add(self.pinky)
        self.ghosts.add(self.inky)
        self.ghosts.add(self.blinky)
        self.ghosts.add(self.clyde)

    def load_data(self):
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, self.ai_settings.hs_file), 'w') as f:
            try:
                self.ai_settings.high_score = int(f.read())
            except:
                self.ai_settings.high_score = 0

    def play(self):
        eloop = EventLoop(self.ai_settings.finished)
        self.load_data()

        while not eloop.finished:
            eloop.check_events(self.ai_settings, self.menu, self.pacman)
            self.pacman.check_dot_collision(self.ai_settings, self.maze.dots, self.maze.pills, self.sb)
            self.sb.check_high_score(self.sb)
            self.update_screen()
            self.pacman.check_wall_collision(self.maze.bricks)
            self.pinky.check_wall_collision(self.maze.bricks)
            self.inky.check_wall_collision(self.maze.bricks)
            self.blinky.check_wall_collision(self.maze.bricks)
            self.clyde.check_wall_collision(self.maze.bricks)
            self.pacman.update()
            self.ghosts.update()
            eloop.update_collisions(self.ai_settings, self.pacman, self.ghosts)

    def update_screen(self):
        self.screen.fill(Game.BLACK)

        if not self.ai_settings.finished:
            self.menu.draw_menu()
            self.sb.check_high_score(self.sb)
            self.sb.prep_high_score()
            self.sb.display_high_score()

        else:
            self.maze.blitme()
            self.pacman.blitme()
            self.pinky.blitme()
            self.inky.blitme()
            self.blinky.blitme()
            self.clyde.blitme()
            self.sb.show_score()

        pygame.display.flip()


game = Game()
game.play()