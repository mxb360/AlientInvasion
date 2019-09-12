import pygame

class BackGround(object):

    def __init__(self, bg_img, screen):
        """ 背景效果 """
        self.img = pygame.image.load(bg_img).convert_alpha()
        self.rect = self.img.get_rect()
        self.screen = screen

    def blitme(self):
        """ 绘制背景 """
        self.screen.blit(self.img, self.rect)
