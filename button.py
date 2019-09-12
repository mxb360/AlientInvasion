import pygame.font

class Button(object):
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 400, 100
        self.button_color = (0, 255, 0)
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 68)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.msg_image = None
        self.msg_image_rect = None
        self.pre_msg(msg)

    def pre_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
