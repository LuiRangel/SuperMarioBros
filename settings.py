import pygame


class Settings:
    def __init__(self):
        # screen settings
        self.bg_color = (130, 190, 245)
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_half_width = self.screen_width / 2

        # music
        self.theme = pygame.mixer.music.load('sounds/super_mario_bros_theme.wav')
        self.jump_sound = pygame.mixer.Sound('sounds/jump.wav')
        self.death = pygame.mixer.Sound('sounds/death.wav')

        # game_active flag
        self.finished = False
        self.display_lives = False

        # player settings
        self.player_speed = 1
        self.player_acc = 0.02  # 0.01
        self.player_jump_acc = 4
        self.player_friction = -0.012
        self.gravity = 0.015
        self.mario_lives = 3

        # scoring
        self.score = 0
        self.high_score = 0
        self.coins = 0
        self.time = 300
        self.hs_file = 'highscore.txt'
