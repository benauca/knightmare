import pygame

from os import path
from bullet import Bullet
from bat import Bat
from player import Player
from monster import Monster
from background import BLACK_COLOR, FPS, SCREEN_HEIGHT, SCREEN_WIDTH, img_dir, WHITE_COLOR


'''number_bullets = 0'''
bullet_limit = 5
score = 0

class Knightmare():

    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # Game loop
        self.running = True
        
        pygame.display.set_caption("Knightmare!")
        pygame.display.set_icon(pygame.image.load(path.join(img_dir,'player.png')).convert())
        
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.player = Player()
        self.bat = Bat()
        self.monster = Monster()

        self.all_sprites.add(self.player)
        self.all_sprites.add(self.bat)
        self.all_sprites.add(self.monster)
        
    '''Game Loop'''
    def run(self) -> None:

        start = pygame.time.get_ticks()

        # keep loop running at the right speed
        self.clock.tick(FPS)
        # Process input (events)

        '''Draw enemies every 5 seconds'''
        now = pygame.time.get_ticks()
        # When 20000 ms have passed.
        ''' if now - start > 100:
            start = now
            bat = Bat()
            all_sprites.add(bat)
        '''
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if Bullet.number_bullets < bullet_limit:
                        Bullet.number_bullets = Bullet.number_bullets + 1
                        self.player.shoot(self.all_sprites)
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
        # Draw / render
        self.screen.fill(WHITE_COLOR)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    def screen_score(self):
        self.image = pygame.image.rect
        self.image.x = SCREEN_HEIGHT / 4

knightmare = Knightmare()
'''knightmare.show_start_screen()'''
while knightmare.running:
    knightmare.run()
    '''g.show_go_screen()'''

pygame.quit()

