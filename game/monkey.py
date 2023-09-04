import pygame


class Monkey(pygame.sprite.Sprite):
    def __init__(self,base_dir):
        pygame.sprite.Sprite.__init__(self)
        position = 400, 510
        self.speed = [0, 0]
        self.img = pygame.image.load(base_dir+'/resources/monkey.png')
        self.rect = self.img.get_rect()
        self.rect.center = position
        self.image = self.img

    def move_left(self):
        self.speed = [-5, 0]
        if self.rect.left < 0:
            self.rect.left = 0
        else:
            self.rect = self.rect.move(self.speed)

    def move_right(self):
        self.speed = [5, 0]
        if self.rect.right > 450:
            self.rect.right = 450
        else:
            self.rect = self.rect.move(self.speed)

    def move_up(self):
        self.speed = [0, -5]
        if self.rect.top < 0:
            self.rect.top = 0
        else:
            self.rect = self.rect.move(self.speed)

    def move_down(self):
        self.speed = [0, 5]
        if self.rect.bottom > 560:
            self.rect.bottom = 560
        else:
            self.rect = self.rect.move(self.speed)
