import pygame
from random import randint
from pygame.sprite import Sprite

class Alient(Sprite):
    """ 表示单个外星人的类 """

    def __init__(self, ai_settings, screen, alient_type):
        """ 初始化外星人并设置其位置 """
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_settings
        self.type = alient_type

        image = pygame.image.load(ai_settings.alient_img[self.type]).convert_alpha()
        self.image = pygame.transform.scale(image, (ai_settings.alient_width[self.type],
                                                    ai_settings.alient_height[self.type]))
        self.rect = self.image.get_rect()

        # 每个外星人在屏幕最上方随机位置出现
        self.rect.centerx = randint(0, self.screen_rect.right)
        self.rect.centery = -self.rect.width

        self.speed_factor = ai_settings.alient_speed_factor[self.type]

    def update(self):
        self.rect.centery += self.speed_factor


    def blitme(self):
        """ 在指定位置绘制外星人 """
        self.screen.blit(self.image, self.rect)


    def __str__(self):
        return 'Alient(%d, %d)' % (self.rect.centerx, self.rect.centery)
