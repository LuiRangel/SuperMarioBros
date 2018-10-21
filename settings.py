class Settings:
    def __init__(self):
        # screen settings
        self.bg_color = (33, 150, 243)
        self.screen_width = 800
        self.screen_height = 800

        # game_active flag
        self.finished = False

        #scoring
        self.score = 0
        self.high_score = 0
        self.hs_file = 'highscore.txt'
