import pygame

class Ship(object):
    def __init__(self, screen, ai_setting, stats):
        """ 初始化飞船并设置其初始位置 """
        self.screen = screen
        self.ai_setting = ai_setting
        self.stats = stats

        # 加载飞船图像并获取其外接矩形
        image = pygame.image.load(ai_setting.ship_img).convert_alpha()
        self.image = pygame.transform.scale(image, (ai_setting.ship_width, ai_setting.ship_height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def reset(self):
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

        self.stats.is_ship_hit = False
        self.stats.ship_reborn_time = 0

    def update(self, sound):
        if self.stats.is_ship_hit:
            self.stats.ship_reborn_time += 1
            if self.stats.ship_reborn_time == self.ai_setting.ship_reborn_time:
                self.stats.ship_life -= 1
                if self.stats.ship_life == 0:
                    print('game over!')
                    self.stats.game_over = True
                    sound.stop_bg()
                    sound.play_gameover()
                    self.stats.game_active = False
                else:
                    self.reset()
            return

        if self.moving_right and self.rect.centerx < self.screen_rect.right - self.ai_setting.ship_speed_factor:
            self.rect.centerx += self.ai_setting.ship_speed_factor
        elif self.moving_left and self.rect.centerx > self.screen_rect.left + self.ai_setting.ship_speed_factor:
            self.rect.centerx -= self.ai_setting.ship_speed_factor

        if self.moving_up and self.rect.centery > self.screen_rect.top + self.ai_setting.ship_speed_factor:
            self.rect.centery -= self.ai_setting.ship_speed_factor
        elif self.moving_down and self.rect.centery < self.screen_rect.bottom - self.ai_setting.ship_speed_factor:
            self.rect.centery += self.ai_setting.ship_speed_factor


    def blitme(self):
        """ 在指定位置绘制飞船 """
        if not self.stats.is_ship_hit:
            self.screen.blit(self.image, self.rect)
