import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ 一个对飞船发射的子弹进行管理的类 """

    def __init__(self, ai_settings, screen, ship):
        """ 在飞船所在处的位置创建一个子弹对象 """
        super().__init__()
        self.screen = screen

        image = pygame.image.load(ai_settings.bullet_ship_img).convert_alpha()
        self.image = pygame.transform.scale(image, (ai_settings.bullet_ship_width, ai_settings.bullet_ship_height))
        self.rect = self.image.get_rect()

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.speed_factor = ai_settings.bullet_ship_speed_factor

    def update(self):
        """ 向上移动子弹 """
        self.rect.y -= self.speed_factor

    def draw_bullet(self):
        """ 在屏幕上绘制子弹 """
        self.screen.blit(self.image, self.rect)

    def __str__(self):
        return 'Bullet(%d, %d)' % (self.rect.centerx, self.rect.centery)
