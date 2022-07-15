import pygame
from os import path
from background import SCREEN_WIDTH

class Monster(pygame.sprite.Sprite):

    SPEED = .5

    WEIGHT = 45
    HEIGHT = 45
    
    character_folder = 'monster'

    def __init__(self):
        """Inicializamos la clase Player."""
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        self.image03 = pygame.image.load(path.join(path.dirname(__file__), "assets", "enemies",self.character_folder, 'ghost-04.png'))
        self.image03 = pygame.transform.scale(self.image03, (self.WEIGHT, self.HEIGHT))
        
        self.image04 = pygame.image.load(path.join(path.dirname(__file__), "assets", "enemies",self.character_folder, 'ghost-05.png'))
        self.image04 = pygame.transform.scale(self.image04, (self.WEIGHT, self.HEIGHT))
        
        self.image05 = pygame.image.load(path.join(path.dirname(
            __file__), "assets", "enemies", self.character_folder, 'ghost-06.png'))
        self.image05 = pygame.transform.scale(self.image05, (self.WEIGHT, self.HEIGHT))
        
        self.image06 = pygame.image.load(path.join(path.dirname(__file__), "assets", "enemies",self.character_folder, 'ghost-07.png'))
        self.image06 = pygame.transform.scale(self.image06, (self.WEIGHT, self.HEIGHT))
        
        self.image07 = pygame.image.load(path.join(path.dirname(__file__), "assets", "enemies",self.character_folder, 'ghost-08.png'))
        self.image07 = pygame.transform.scale(self.image07, (self.WEIGHT, self.HEIGHT))
        
        self.image08 = pygame.image.load(path.join(path.dirname(__file__), "assets", "enemies",self.character_folder, 'ghost-09.png'))
        self.image08 = pygame.transform.scale(self.image08, (self.WEIGHT, self.HEIGHT))        
        
        self.sprites.append(self.image03)
        self.sprites.append(self.image04)
        self.sprites.append(self.image05)
        self.sprites.append(self.image06)
        self.sprites.append(self.image07)
        self.sprites.append(self.image08)
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.y_pos = 0

        self.rect.centerx = SCREEN_WIDTH  / 3

        """ Posiition on init"""
    def update(self):
        if self.y_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.y_pos >= SCREEN_WIDTH - 20:
            self.SPEED = -abs(self.SPEED)
        self.y_pos += self.SPEED
        self.rect.centery = self.y_pos

    ''' speed es la velociad en la que se cambia un sprite'''

    def animate(self, speed):
        """Movement Player."""

        self.current_sprite += speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]
