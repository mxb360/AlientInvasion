import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from background import BackGround
from game_stats import  GameStats
from button import Button
from scoreboard import Scoreboard
from sound import Sound
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('外星人入侵')

    play_button = Button(screen, "Start Game")
    sound = Sound(ai_settings)
    bg = BackGround(ai_settings.bg_image, screen)

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(screen, ai_settings, stats)

    bullets = Group()
    alients = Group()
    explosions = Group()

    ALIENT_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENT_EVENT, ai_settings.alient_create_time)
    sound.play_title()

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, alients, ALIENT_EVENT, play_button, sb, sound)
        ship.update(sound)
        gf.update_alients(screen, ship, alients, ai_settings, explosions, sb)
        gf.update_bullets(screen, ai_settings, alients, bullets, explosions, sb)
        gf.update_explosions(explosions)
        gf.update_screen(ship, bg, bullets, alients, explosions, play_button, sb)

run_game()
