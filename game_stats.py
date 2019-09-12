class GameStats(object):
    """ 跟踪游戏的条统计信息 """

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.ship_life = self.ai_settings.ship_limit
        self.is_ship_hit = False
        self.ship_reborn_time = 0
        self.game_active = False
        self.score = 0
        self.hit_count = 0
        self.lost_count = 0
        self.game_over = False

        self.reset()

    def reset(self):
        """ 初始化在游戏运行期间可能变化的统计信息 """
        self.ship_life = self.ai_settings.ship_limit
        self.is_ship_hit = False
        self.game_over = False
        self.ship_reborn_time = 0
        self.score = 0
        self.hit_count = 0
        self.lost_count = 0
