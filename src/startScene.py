from locale import setlocale
from pygame.locals import *
import time
import pygame
from os import path
from parent import ParentScene
from background import Background


class StartSprite(pygame.sprite.Sprite):

    folder = 'scene'
   
    def __init__(self):
        '''Init The game Character.'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            path.join(Background.img_dir, self.folder, "start-scene.png"))

        self.rect = self.image.get_rect()
        self.rect.centerx = Background.SCREEN_WIDTH / 2
        self.rect.centery = Background.SCREEN_HEIGHT / 2.5
        
        self.x_pos = Background.SCREEN_WIDTH / 2
        self.y_pos = Background.SCREEN_HEIGHT / 3


    def draw(self):
        
        self.rect.centerx = self.x_pos
        self.rect.centery = self.y_pos

    
class StartScene(ParentScene):

    WEIGHT = Background.SCREEN_WIDTH
    HEIGHT = Background.SCREEN_HEIGHT/4

    TEXT_PULSE_SPACE_TO_START = 'Pulse Space Key!'
    TEXT_START_GAME = 'Start Game'

    SPEED = 0.05
    colors = []
    current_color = 0
    colors.append(pygame.Color("white"))
    colors.append(pygame.Color("black"))


    folder = 'scene'
   
    def __init__(self) -> None:
        ParentScene.__init__(self)
        self.running = True

        self.startSprite = StartSprite()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.startSprite)

        self.font = pygame.font.SysFont(None, 48)
        self.textPulse = self.font.render('Pulse Start!!', True, Background.WHITE_COLOR)
        self.tRect = self.textPulse.get_rect()

    def processEvents(self, events):
        """Procesa los eventos recibidos en la escena"""

        for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.screen.fill(pygame.Color("black"))
                        self.textPulse = self.font.render(self.TEXT_START_GAME, False, self.colors[0])
                        self.screen.blit(self.textPulse, (self.tRect.x, self.tRect.y))
                        pygame.display.flip()            
                        time.sleep(1)
                        self.running = False
                        self.nextScene = True
                        self.toScene = 'LevelOne'


    def run(self) -> None:
        super().run()
        # Update
        self.screen.fill(pygame.Color("black"))
        # Aplicamos el color al texto
        self.current_color += self.SPEED
        if self.current_color >= len(self.colors):
            self.current_color = 0
        
        self.textPulse = self.font.render(self.TEXT_PULSE_SPACE_TO_START,
                        False, self.colors[int(self.current_color)])

    
    def draw(self, screen) -> None:
        super().draw(screen)
        self.tRect.x = Background.SCREEN_WIDTH /2 - 50
        self.tRect.y = Background.SCREEN_HEIGHT - 45
        screen.fill(Background.BLACK_COLOR)
        screen.blit(self.startSprite.image, self.startSprite.rect)
        screen.blit(self.textPulse, (self.tRect.x, self.tRect.y)) 
