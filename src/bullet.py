import pygame
from os import path
from background import Background

class Bullet(pygame.sprite.Sprite):

    IMAGE = 'arrow.png'
    number_bullets = 0

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        '''self.image = pygame.image.load(path.join(img_dir, self.IMAGE))'''
        self.image = pygame.image.load(path.join(path.dirname(__file__), "assets",
                                                        "weapons", self.IMAGE))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.bottom = y + 10
        self.rect.centerx = x
        self.speedy = 10

    def update(self):
        self.rect.y -= self.speedy
        '''global number_bullets'''
        if not Background.SCREEN_HEIGHT > abs(self.rect.y):
            Bullet.number_bullets = Bullet.number_bullets - 1
            self.kill()
