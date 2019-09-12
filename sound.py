import pygame

class Sound(object):
    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.bg_sound = pygame.mixer.Sound(ai_setting.bg_music)
        self.fire_sound = pygame.mixer.Sound(ai_setting.fire_music)
        self.title_sound = pygame.mixer.Sound(ai_setting.title_music)
        self.gameover = pygame.mixer.Sound(ai_setting.gameover_music)

    def play_bg(self):
        self.bg_sound.play(-1)

    def stop_bg(self):
        self.bg_sound.stop()

    def play_gameover(self):
        self.gameover.play()

    def stop_gameover(self):
        self.gameover.stop()

    def play_fire(self):
        self.fire_sound.play()

    def play_title(self):
        self.title_sound.play()

    def stop_title(self):
        self.title_sound.stop()
