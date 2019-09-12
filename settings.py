class Settings(object):
    """ 存储《外星人入侵》的所有设置 """

    def __init__(self):
        """ 初始化游戏的设置 """

        # 屏幕设置
        self.screen_width  = 1400
        self.screen_height = 875
        self.bg_color = (130, 230, 230)

        # 背景设置
        self.bg_image = 'images/bg.jpg'
        self.bg_music = 'music/bg.wav'
        self.title_music = 'music/title.wav'
        self.gameover_music = 'music/gameover.wav'

        # 飞船设置
        self.ship_speed_factor = 10
        self.ship_img = 'images/ship.png'
        self.ship_width = 147
        self.ship_height = 100
        self.ship_limit = 3
        self.ship_reborn_time = 10
        self.life_image = self.ship_img
        self.life_width = 50
        self.life_height = 40

        # 子弹设置
        self.bullet_ship_img = 'images/bullet_ship.png'
        self.bullet_ship_width = 20
        self.bullet_ship_height = 80
        self.bullet_ship_speed_factor = 20
        self.bullet_ship_allowed = 10
        self.fire_music = 'music/fire.wav'

        # 外星人设置
        self.alient_img = ["images/alient%d.png" % i for i in range(6)]
        self.alient_width = (100, 80, 100, 80, 50, 50)
        self.alient_height = (100, 80, 100, 80, 50, 50)
        self.alient_speed_factor = (1, 3, 1, 3, 5, 5)
        self.alient_score_points = (100, 200, 100, 200, 300, 300)

        self.alient_create_fre = 3
        self.alient_create_time = 500
        self.alient_allowed = 100
        self.alient_types = len(self.alient_img)

        # 爆炸
        self.explosion_img = 'images/explosion.png'
        self.explosion_size = (6, 1)
        self.explosion_count = 6
        self.explosion_time = 7
