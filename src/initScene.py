from ast import Str
import pygame
from os import path
from parent import ParentScene
from background import Background


class InitScene(ParentScene):
    SPEED = .5
    WEIGHT = Background.SCREEN_WIDTH
    HEIGHT = Background.SCREEN_HEIGHT/4
    
    def __init__(self) -> None:
        ParentScene.__init__(self)
        self.brand = Brand()
        self.all_sprites.add(self.brand)
        self.nextScene = False
        self.running = True
   
    def run(self) -> None:
        super().run()
        # Update
        self.all_sprites.update()
        

    
    def draw(self, screen) -> None:
        self.all_sprites.draw(screen)
        if self.brand.y_pos > Background.SCREEN_WIDTH / 3:
            self.brand.y_pos -= self.SPEED
        else:
            self.running = False
            self.nextScene = True
            self.toScene = 'Start'
            
        self.brand.rect.centerx = self.brand.x_pos
        self.brand.rect.centery = self.brand.y_pos

    def toScene(self, toScene):
        self.toScene = toScene

class Brand(pygame.sprite.Sprite):

    folder = 'scene'

    def __init__(self):
        '''Init The game Character.'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            path.join(Background.img_dir, self.folder, "init-scene.png"))

        self.rect = self.image.get_rect()
        self.rect.centerx = Background.SCREEN_WIDTH / 3

        self.x_pos = Background.SCREEN_WIDTH / 2
        self.y_pos = Background.SCREEN_HEIGHT

        """ Posiition on init"""



    

