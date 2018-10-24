import pygame


class Settings:
    def __init__(self):
        # screen settings
        self.screen_width = 975
        self.screen_height = 1200
        self.BLACK = 0, 0, 0

        # Music and Sounds
        #pygame.mixer.music.load('sounds/maintheme.wav')
        #self.waka = pygame.mixer.Sound('sounds/waka.wav')
        #self.dead = pygame.mixer.Sound('sounds/dead.wav')

        #pacman settings
        self.pacman_speed = 1
        self.lives = 2

        #ghost settings
        self.ghost_speed = 1
        self.pinky_direction = 1
        self.inky_direction = 1
        self.blinky_direction = 1
        self.clyde_direction = 1

        # game_active flag
        self.finished = False
        self.menu_active = False

        #scoring
        self.score = 0
        self.high_score = 0
        self.dot_points = 10
        self.pill_points = 30
        self.hs_file = 'highscore.txt'