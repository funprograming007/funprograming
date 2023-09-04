import os
import sys

import pygame
from pygame import K_LEFT, K_RIGHT, K_UP, K_DOWN

from game.banana import Banana
from game.monkey import Monkey


def start_game():
    base_dir = '.'
    if hasattr(sys, '_MEIPASS'):
        base_dir = os.path.join(sys._MEIPASS)

    pygame.init()
    size = width, height = 450, 560
    screen = pygame.display.set_mode(size)
    bg = pygame.image.load(base_dir+'/resources/background.png')
    pygame.display.set_caption("游戏")
    mk = Monkey(base_dir)
    group = pygame.sprite.Group()
    i = 0
    score = 0

    pygame.mixer.music.load(base_dir+'/resources/background.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()

    win_sound = pygame.mixer.Sound(base_dir+'/resources/win.wav')
    win_sound.set_volume(1)

    while True:
        # 处理程序退出
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        #处理键盘
        key = pygame.key.get_pressed()
        if key[K_LEFT]:
            mk.move_left()
        if key[K_RIGHT]:
            mk.move_right()
        if key[K_UP]:
            mk.move_up()
        if key[K_DOWN]:
            mk.move_down()
        screen.blit(bg, bg.get_rect())
        screen.blit(mk.image, mk.rect)

        # paint scores
        font_big = pygame.font.Font(base_dir+"/resources/msyhbd.ttc", 40)
        score_text = f'Score: {score}'
        score_text = font_big.render(score_text, True, (0, 255, 0))
        score_rect = score_text.get_rect()
        score_rect.topleft = [5, 5]
        screen.blit(score_text, score_rect)

        #随机生成香蕉
        i = i + 1
        if i % 40 == 0:
            newbanana = Banana(base_dir)
            group.add(newbanana)
        for banana in group.sprites():
            banana.move()
            screen.blit(banana.img, banana.rect)
            if pygame.sprite.collide_mask(mk, banana):
                group.remove(banana)
                win_sound.play()
                score += 1
        pygame.display.update()
        pygame.time.Clock().tick(60)


if __name__ == '__main__':
    start_game()
