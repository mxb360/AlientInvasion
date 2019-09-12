import sys
import pygame
from bullet import Bullet
from alient import Alient
from explosion import Explosion
from random import randint


def check_keydown_events(ai_settings, screen, event, ship, bullets, sound):
    """ 响应按键按下 """
    if event.key == pygame.K_q:
        sys.exit()
    if not ship.stats.game_active:
        return
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        sound.play_fire()
        fire_bullet(ai_settings, screen, ship, bullets)
        pygame.time.set_timer(pygame.USEREVENT + 2, 100)



def check_keyup_events(event, ship):
    """ 响应按键松开 """
    if not ship.stats.game_active:
        return
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_SPACE:
        pygame.time.set_timer(pygame.USEREVENT + 2, 0)


def check_events(ai_settings, screen, ship, bullets, alients, alient_event, play_button, sb, sound):
    """ 响应键盘和鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings, screen, event, ship, bullets, sound)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == alient_event:
            if ship.stats.game_active or ship.stats.game_over:
                create_alient(ai_settings, screen, alients)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_nutton(ship.stats, play_button, mouse_x, mouse_y, ship, alients, bullets, sb, sound)
        elif event.type == pygame.USEREVENT + 2:
            if ship.stats.is_ship_hit:
                pygame.time.set_timer(pygame.USEREVENT + 2, 0)
            sound.play_fire()
            fire_bullet(ai_settings, screen, ship, bullets)

def check_play_nutton(stats, play_button, mouse_x, mouse_y, ship, alients, bullets, sb, sound):
    """ 检测按钮是否被点击 """
    if stats.game_active:
        return
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        game_restart(ship, alients, bullets, stats, sound, sb)


def check_bullet_alient_collisions(screen, ai_settings, alients, bullets, explosions, sb):
    """ 检测子弹是否击中外星人 """
    collisions = pygame.sprite.groupcollide(bullets, alients, True, True)
    if collisions:
        for bullet, alients in collisions.items():
            for alient in alients:
                explosion = Explosion(screen, ai_settings.explosion_img,
                                      (alient.rect.left, alient.rect.top), ai_settings.explosion_size,
                                      ai_settings.explosion_count, ai_settings.explosion_time)
                explosions.add(explosion)
                sb.stats.score += ai_settings.alient_score_points[alient.type]
                sb.stats.hit_count += 1
                sb.pre_score()
                sb.pre_hit_count()


def check_alient_ship_collisions(screen, ai_settings, ship, alients, explosions):
    """ 检测外星人是否击中飞船"""
    alient = pygame.sprite.spritecollideany(ship, alients)
    if alient and not ship.stats.is_ship_hit:
        explosion = Explosion(screen, ai_settings.explosion_img,
                              (ship.rect.left, ship.rect.top), ai_settings.explosion_size,
                              ai_settings.explosion_count, ai_settings.explosion_time)
        explosions.add(explosion)
        explosion = Explosion(screen, ai_settings.explosion_img,
                              (alient.rect.left, alient.rect.top), ai_settings.explosion_size,
                              ai_settings.explosion_count, ai_settings.explosion_time)
        explosions.add(explosion)
        alients.remove(alient)
        ship.stats.is_ship_hit = True

def fire_bullet(ai_settings, screen, ship, bullets):
    """ 开火 """
    if len(bullets) < ai_settings.bullet_ship_allowed:
        bullets.add(Bullet(ai_settings, screen, ship))

def create_alient(ai_settings, screen, alients):
    """ 创建外星人 """
    if len(alients) >= ai_settings.alient_allowed:
        return
    rand = randint(1, ai_settings.alient_create_fre)
    if rand == 1:
        alients.add(Alient(ai_settings, screen, randint(0, ai_settings.alient_types - 1)))

def game_restart(ship, alients, bullets, stats, sound, sb):
    """ 重新开始游戏 """
    sound.stop_title()
    sound.stop_gameover()
    sound.play_bg()
    stats.game_active = True
    alients.empty()
    bullets.empty()
    ship.reset()
    stats.reset()
    sb.pre_all()

def update_screen(ship, bg, bullets, alients, explosions, play_button, sb):
    """ 更新屏幕上的图像，并切换到新屏幕 """
    bg.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for alient in alients.sprites():
        alient.blitme()
    for explosion in explosions.sprites():
        explosion.blitme()
    ship.blitme()
    sb.show()
    if not ship.stats.game_active:
        play_button.draw()

    # 让最近的绘制的屏幕可见
    pygame.display.flip()

def update_bullets(screen, ai_settings, alients, bullets, explosions, sb):
    """ 更新子弹的位置，并删除已消失的子弹 """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alient_collisions(screen, ai_settings, alients, bullets, explosions, sb)


def update_alients(screen, ship, alients, ai_settings, explosions, sb):
    """ 更新外星人的位置 """
    alients.update()
    for alient in alients.copy():
        if alient.rect.top > ai_settings.screen_height:
            alients.remove(alient)
            if ship.stats.game_active:
                sb.stats.lost_count += 1
                lost_score = ai_settings.alient_score_points[alient.type] // 2
                if sb.stats.score - lost_score > 0:
                    sb.stats.score -= lost_score
                    sb.pre_score()
                sb.pre_lost_count()
    check_alient_ship_collisions(screen, ai_settings, ship, alients, explosions)


def update_explosions(explosions):
    """ 更新爆炸效果 """
    explosions.update()
    for explosion in explosions.copy():
         if explosion.frame == explosion.frame_count - 1:
             explosions.remove(explosion)
