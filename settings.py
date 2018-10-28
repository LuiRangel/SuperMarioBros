import pygame


class Settings:
    def __init__(self):
        # screen settings

        self.bg_color = (130, 190, 245)
        self.screen_width = 1200
        self.screen_height = 800

        # music
        self.theme = pygame.mixer.music.load('sounds/super_mario_bros_theme.wav')

        # game_active flag
        self.finished = False

        # scoring
        self.score = 0
        self.high_score = 0
