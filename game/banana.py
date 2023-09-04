from random import randint

import pygame


class Banana(pygame.sprite.Sprite):
    def __init__(self,base_dir):
        pygame.sprite.Sprite.__init__(self)
        x = randint(20, 430)
        position = [x, 20]
        speed = [0, 3]
        self.img = pygame.image.load(base_dir+'/resources/banana.png')
        self.rect = self.img.get_rect()
        self.rect.center = position
        self.image = self.img
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)

