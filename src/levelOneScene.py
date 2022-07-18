from parent import ParentScene
import pygame

from bullet import Bullet
from bat import Bat
from player import Player
from monster import Monster


'''number_bullets = 0'''
bullet_limit = 5
score = 0

class LevelOneScene(ParentScene):

    def __init__(self) -> None:
        ParentScene.__init__(self)
        self.running = True
        self.nextScene = False

        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.player = Player()
        self.bat = Bat()
        self.monster = Monster()

        self.all_sprites.add(self.player)
        self.all_sprites.add(self.bat)
        self.all_sprites.add(self.monster)
        
    '''Scene Loop'''
    def run(self) -> None:
        super().run()
        for bullet in self.player.bullets:
            if self.bat.rect.colliderect(bullet.rect):
                bullet.kill()
                Bullet.number_bullets = Bullet.number_bullets -1
                self.bat.kill()
        # Update
        self.all_sprites.update()
        self.player.animate(0.15)
        self.bat.animate(0.15)
        self.monster.animate(0.15)

    
    def draw(self, screen) -> None:
        self.all_sprites.draw(screen)
        

    
    def processEvents(self, events):
        
        for event in events:
            # check for closing window
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if Bullet.number_bullets < bullet_limit:
                        Bullet.number_bullets = Bullet.number_bullets + 1
                        self.player.shoot(self.all_sprites)

    def toScene(self, toScene):
        self.toScene = toScene