import pygame
from os import path
from background import Background

class Bat(pygame.sprite.Sprite):
    
    SPEED_X = -3
    SPEED_Y = 1
    gravity_y = 10
    WEIGHT = 35
    HEIGHT = 35
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
        self.rect.centerx = Background.SCREEN_WIDTH / 3
        
        self.x_pos = Background.SCREEN_WIDTH / 3
        self.y_pos = 5

    def update(self):
        
        if self.x_pos >= Background.SCREEN_WIDTH - 20 or self.x_pos <= 10:
            self.SPEED_X *= -1
            self.y_pos += self.gravity_y
            
        self.x_pos += self.SPEED_X
        self.y_pos += self.SPEED_Y
        self.rect.centerx = self.x_pos
        self.rect.centery = self.y_pos

    def animate(self, speed):
        """Movement Player."""
        
        self.current_sprite += speed
        
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        
        self.image = self.sprites[int(self.current_sprite)]

    def remove(self, all_sprites):

        self.x_pos = self.rect.centerx = Background.SCREEN_WIDTH
        self.y_pos = self.rect.centery = Background.SCREEN_HEIGHT 
        self.SPEED_X = self.SPEED_Y = self.gravity_y = 0
        all_sprites.remove(self)
        self.kill
                    