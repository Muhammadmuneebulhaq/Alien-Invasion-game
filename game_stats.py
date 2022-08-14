class GameStats:
    '''track game statictics'''
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.highscore = 0
        
    def reset_stats(self):
        self.rockets_left = self.settings.rocket_limit
        self.score = 0
        self.level = 1