
import pygame
from os import path
from bullet import Bullet
from background import FPS, SCREEN_HEIGHT, SCREEN_WIDTH

class Player(pygame.sprite.Sprite):
    """Clase que representa la nave del jugador."""

    WEIGHT = 50
    HEIGHT = 50
    character_folder = 'character'

    def __init__(self):
        """Inicializamos la clase Player."""
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        self.image00 = pygame.image.load(path.join(path.dirname(__file__), "assets", self.character_folder, 'tile000.png'))
        self.image00 = pygame.transform.scale(self.image00, (self.WEIGHT, self.HEIGHT))
        
        self.image01 = pygame.image.load(path.join(path.dirname(__file__), "assets", self.character_folder, 'tile001.png'))
        self.image01 = pygame.transform.scale(self.image01, (self.WEIGHT, self.HEIGHT))
        
        self.image02 = pygame.image.load(path.join(path.dirname(__file__), "assets", self.character_folder, 'tile002.png'))
        self.image02 = pygame.transform.scale(self.image02, (self.WEIGHT, self.HEIGHT))
        
        self.image03 = pygame.image.load(path.join(path.dirname(__file__), "assets", self.character_folder, 'tile003.png'))
        self.image03 = pygame.transform.scale(self.image03, (self.WEIGHT, self.HEIGHT))
        
        self.image04 = pygame.image.load(path.join(path.dirname(__file__), "assets", self.character_folder, 'tile004.png'))
        self.image04 = pygame.transform.scale(self.image04, (self.WEIGHT, self.HEIGHT))
        
        self.image05 = pygame.image.load(path.join(path.dirname(
            __file__), "assets", self.character_folder, 'tile005.png'))
        self.image05 = pygame.transform.scale(self.image05, (self.WEIGHT, self.HEIGHT))
        
        self.sprites.append(self.image00)
        self.sprites.append(self.image01)
        self.sprites.append(self.image02)
        self.sprites.append(self.image03)
        self.sprites.append(self.image04)
        self.sprites.append(self.image05)
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        """ Posiition on init"""
        self.rect.centerx = SCREEN_WIDTH + 50
        self.rect.bottom = SCREEN_HEIGHT / 2
        self.speedx = 0
        self.speedy = 0
        self.SPEED = 5
        self.bullets = pygame.sprite.Group()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

    def update(self):
    
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = - self.SPEED
        if keystate[pygame.K_RIGHT]:
            self.speedx = self.SPEED
        if keystate[pygame.K_UP]:
            self.speedy = -self.SPEED
        if keystate[pygame.K_DOWN]:
            self.speedy = self.SPEED
        if self.rect.right > self.SCREEN_WIDTH:
            self.rect.right = self.SCREEN_WIDTH
        if self.rect.bottom > self.SCREEN_HEIGHT:
            self.rect.bottom = self.SCREEN_HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def shoot(self, all_sprites):
        '''all_sprites = pygame.sprite.Group()'''
        bullet = Bullet(self.rect.centerx, self.rect.bottom)
        all_sprites.add(bullet)
        self.bullets.add(bullet)
    
    ''' speed es la velociad en la que se cambia un sprite'''
    def animate(self, speed):
        """Movement Player."""
        
        self.current_sprite += speed
        
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        
        self.image = self.sprites[int(self.current_sprite)]
