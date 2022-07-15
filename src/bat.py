import pygame
from os import path
from background import SCREEN_WIDTH

class Bat(pygame.sprite.Sprite):
    SPEED = 2.5
    WEIGHT = 50
    HEIGHT = 50
    bat_folder = 'bat'
   
    def __init__(self):
        '''Init The game Character.'''
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        self.image01 = pygame.image.load(path.join(path.dirname(__file__), "assets",
                                                        "enemies", self.bat_folder, 'bat-001.png'))
        self.image01 = pygame.transform.scale(self.image01, (self.WEIGHT, self.HEIGHT))
        self.image02 = pygame.image.load(path.join(path.dirname(__file__), "assets",
                                                        "enemies", self.bat_folder, 'bat-002.png'))
        self.image02 = pygame.transform.scale(
            self.image02, (self.WEIGHT, self.HEIGHT))
        self.image03 = pygame.image.load(path.join(path.dirname(__file__), "assets",
                                                        "enemies", self.bat_folder, 'bat-003.png'))
        self.image03 = pygame.transform.scale(
            self.image03, (self.WEIGHT, self.HEIGHT))
        self.image04 = pygame.image.load(path.join(path.dirname(__file__), "assets",
                                                        "enemies", self.bat_folder, 'bat-004.png'))
        self.image04 = pygame.transform.scale(
            self.image04, (self.WEIGHT, self.HEIGHT))
        self.sprites.append(self.image01)
        self.sprites.append(self.image02)
        self.sprites.append(self.image03)
        self.sprites.append(self.image04)

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(
            self.image, (self.WEIGHT, self.HEIGHT))
        
        
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 3
        
        self.x_pos = 150
        self.y_pos = 120
        """ Posiition on init"""
    def update(self):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= SCREEN_WIDTH - 20:
            self.SPEED = abs(self.SPEED)

        self.x_pos += self.SPEED + .5
        self.y_pos += self.SPEED / 5
        self.rect.centerx = self.x_pos
        self.rect.centery = self.y_pos

    ''' speed es la velociad en la que se cambia un sprite'''
    def animate(self, speed):
        """Movement Player."""
        
        self.current_sprite += speed
        
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        
        self.image = self.sprites[int(self.current_sprite)]
