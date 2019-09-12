import pygame.font

class Scoreboard(object):
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (255, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.score_image = None
        self.score_rect = None
        self.hit_count_image = None
        self.hit_count_rect = None
        self.lost_count_image = None
        self.lost_count_rect = None
        self.life_count_image = None
        self.life_count_rect = None

        life_str = 'Life:  '
        self.life_count_image = self.font.render(life_str, True, self.text_color)
        self.life_count_rect = self.life_count_image.get_rect()
        self.life_count_rect.left = 20
        self.life_count_rect.top = 20
        image = pygame.image.load(ai_settings.life_image).convert_alpha()
        self.life_image = pygame.transform.scale(image, (ai_settings.life_width, ai_settings.life_height))
        self.life_rect = self.life_image.get_rect()
        self.life_rect.top = 15
        self.pre_all()
        game_over = 'GAME OVER'
        self.font = pygame.font.SysFont(None, 208)
        self.game_over_image = self.font.render(game_over, True, self.text_color)
        self.font = pygame.font.SysFont(None, 48)
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.centerx = self.screen_rect.centerx
        self.game_over_rect.top = self.lost_count_rect.bottom + 30


    def pre_all(self):
        self.pre_score()
        self.pre_hit_count()
        self.pre_lost_count()

    def pre_score(self):
        score_str = 'Score:  ' + str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = 20
        self.score_rect.top = 10 + self.life_count_rect.bottom

    def pre_hit_count(self):
        hit_count_str = 'Hit:  ' + str(self.stats.hit_count)
        self.hit_count_image = self.font.render(hit_count_str, True, self.text_color)
        self.hit_count_rect = self.hit_count_image.get_rect()
        self.hit_count_rect.left = 20
        self.hit_count_rect.top = 10 + self.score_rect.bottom

    def pre_lost_count(self):
        lost_count_str = 'Lost:  ' + str(self.stats.lost_count)
        self.lost_count_image = self.font.render(lost_count_str, True, self.text_color)
        self.lost_count_rect = self.lost_count_image.get_rect()
        self.lost_count_rect.left = 20
        self.lost_count_rect.top = 10 + self.hit_count_rect.bottom

    def show(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hit_count_image, self.hit_count_rect)
        self.screen.blit(self.lost_count_image, self.lost_count_rect)
        self.screen.blit(self.life_count_image, self.life_count_rect)

        self.life_rect.left = 100
        for i in range(self.stats.ship_life):
            self.screen.blit(self.life_image, self.life_rect)
            self.life_rect.left = self.life_rect.right + 5
        if self.stats.game_over:
            self.screen.blit(self.game_over_image, self.game_over_rect)
