from background import Background
from parent import ParentScene, Resume
import pygame

from bullet import Bullet
from bat import Bat
from player import Player
from monster import Monster
import sys
from random import randint

'''number_bullets = 0'''
bullet_limit = 5

class Tree(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/tree.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


class CameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0]/2
        self.half_y = self.display_surface.get_size()[1]/2

        self.ground_surf = pygame.image.load('assets/scene-01.png').convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(bottomleft=(0, 0))

        # Creamos de manera aleatoria de algunos arboles dentro del mapa
        for i in range(20):
            random_x = randint(0, 800)
            random_y = randint(0, 8000)
            Tree((random_x, random_y), self)

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_y

    def custom_draw(self, player):
        #self.center_target_camera(player)
        groud_offset_pos = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf, groud_offset_pos)
        self.ground_rect.y += 1
 
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
 

class LevelOneScene(ParentScene):

    NUMBER_BATS = 5
    NUMBER_MONSTER = 3
    current_bats = 0
    current_monsters = 0
    time_elapsed_since_last_action = 0

    # Datos de puntuación
    resume = Resume()

    def __init__(self) -> None:
        ParentScene.__init__(self)
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.nextScene = False

        self.bats = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()
        self.all_sprites = CameraGroup()
        self.player = Player((400, 7900), self.all_sprites)
        
        self.start_ticks = pygame.time.get_ticks()
        self.flag = int(pygame.time.get_ticks() / 1000 )


    '''Scene Loop'''

    def run(self) -> None:
        super().run()
        
        difference = (pygame.time.get_ticks() - self.start_ticks) / 1000
        if int(difference) % 10 == 0:
            if self.current_bats < self.NUMBER_BATS:
                dt = self.clock.tick()
                self.time_elapsed_since_last_action += dt
                if self.time_elapsed_since_last_action > 40:
                    bat = Bat()
                    self.bats.add(bat)
                    self.all_sprites.add(bat)
                    self.current_bats += 1
                    self.time_elapsed_since_last_action = 0

        if int(pygame.time.get_ticks() / 1000)  > 5+ self.flag:
                self.flag = int(pygame.time.get_ticks() / 1000 )
                monster = Monster()
                self.monsters.add(monster)
                self.all_sprites.add(monster)
                self.current_monsters +=1

        
        for bullet in self.player.bullets:
            for bat in self.bats:
                if bat.rect.colliderect(bullet.rect):
                    bullet.kill()
                    bat.kill()
                    Bullet.number_bullets = Bullet.number_bullets - 1
                    self.resume.score += 50
                    self.current_bats -= 1
                    self.current_monsters -=1
            for monster in self.monsters:
                if monster.rect.colliderect(bullet.rect):
                    bullet.kill()
                    monster.kill()
                    Bullet.number_bullets = Bullet.number_bullets - 1
                    self.resume.score += 10

        for bat in self.bats:
            if bat.y_pos > Background.HEIGHT_MENU:
                self.current_bats -= 1
                bat.kill()
        for monster in self.monsters:
            if monster.y_pos > Background.HEIGHT_MENU:
                self.current_monsters -=1
                monster.kill()

        ## Kill Player
        for bat in self.bats:
            if bat.rect.colliderect(self.player.rect):
                bat.remove(self.all_sprites)
                self.resume.lifes -= 1

        # Update
        self.all_sprites.update()
        self.all_sprites.custom_draw(self.player)
        ## Debo separar el metodo en draw y update. Afecta al time_elapsed_since_last_action
        self.drawScoreMenu()
        self.drawTimer(self.start_ticks)
        self.player.animate(0.15)
        # self.monster.animate(0.15)
        for bat in self.bats:
            bat.animate(0.15)
        for monster in self.monsters:
            monster.animate(0.15)
        
    def processEvents(self, events):
        self.player.speedx = 0
        self.player.speedy = 0

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

    def drawScoreMenu(self):
        '''Draw the Score Menu'''

        pygame.draw.rect(self.screen, pygame.Color(
            "black"), (0, Background.HEIGHT_MENU, Background.SCREEN_WIDTH, Background.SCREEN_HEIGHT / 4))

        #Establezco el tipo de fuente.
        font = pygame.font.SysFont(None, 48)

        # Create Text
        textScore = font.render("SCORE", True, Background.WHITE_COLOR)
        tScoreRect = textScore.get_rect()
        tScoreRect.x = 50
        tScoreRect.y = Background.SCREEN_HEIGHT - Background.SCREEN_HEIGHT / 4
        self.screen.blit(textScore, (tScoreRect.x, tScoreRect.y))

        scoreAsText = font.render(str(self.resume.score), True, Background.WHITE_COLOR)
        tScoreAsTextRect = scoreAsText.get_rect()
        tScoreAsTextRect.x = tScoreRect.x
        tScoreAsTextRect.y = tScoreRect.x + \
            Background.SCREEN_HEIGHT - Background.SCREEN_HEIGHT / 4
        self.screen.blit(scoreAsText, (tScoreAsTextRect.x, tScoreAsTextRect.y))
        
        
        textHighScore = font.render("HI SCORE", True, Background.WHITE_COLOR)
        tHiScoreRect = textHighScore.get_rect()
        tHiScoreRect.x = tScoreRect.x + Background.SCREEN_WIDTH - 3 *( Background.SCREEN_WIDTH /4)
        tHiScoreRect.y = Background.SCREEN_HEIGHT - Background.SCREEN_HEIGHT / 4
        self.screen.blit(textHighScore, (tHiScoreRect.x, tHiScoreRect.y))

        hiScoreAsText = font.render(str(self.resume.hi_score), True, Background.WHITE_COLOR)
        tHiScoreValueRect = hiScoreAsText.get_rect()
        tHiScoreValueRect.x = tScoreRect.x + \
            Background.SCREEN_WIDTH - 3 * (Background.SCREEN_WIDTH / 4)
        tHiScoreValueRect.y = tScoreRect.x + Background.SCREEN_HEIGHT - Background.SCREEN_HEIGHT / 4
        self.screen.blit(
            hiScoreAsText, (tHiScoreValueRect.x, tHiScoreValueRect.y))


        textRest = font.render("REST", True, Background.WHITE_COLOR)
        tRestRect = textRest.get_rect()
        tRestRect.x = tScoreRect.x + Background.SCREEN_WIDTH / 2
        tRestRect.y = Background.SCREEN_HEIGHT - Background.SCREEN_HEIGHT / 4
        self.screen.blit(textRest, (tRestRect.x, tRestRect.y))

        lifesAsText = font.render(str(self.resume.lifes), True, Background.WHITE_COLOR)
        tLifesAsTextRect = lifesAsText.get_rect()
        tLifesAsTextRect.x = tScoreRect.x + Background.SCREEN_WIDTH / 2
        tLifesAsTextRect.y = tScoreRect.x + Background.SCREEN_HEIGHT - Background.SCREEN_HEIGHT / 4
        self.screen.blit(lifesAsText, (tLifesAsTextRect.x, tLifesAsTextRect.y))


        textStage = font.render("STAGE", True, Background.WHITE_COLOR)
        tStageRect = textStage.get_rect()
        tStageRect.x = tScoreRect.x + Background.SCREEN_WIDTH - Background.SCREEN_WIDTH / 4
        tStageRect.y = Background.SCREEN_HEIGHT - Background.SCREEN_HEIGHT / 4
        self.screen.blit(textStage, (tStageRect.x, tStageRect.y))

        stageAsText = font.render(str(self.resume.level), True, Background.WHITE_COLOR)
        tStageAsTextRect = stageAsText.get_rect()
        tStageAsTextRect.x = tScoreRect.x + Background.SCREEN_WIDTH - Background.SCREEN_WIDTH / 4
        tStageAsTextRect.y = tScoreRect.x + Background.SCREEN_HEIGHT - Background.SCREEN_HEIGHT / 4
        self.screen.blit(stageAsText, (tStageAsTextRect.x, tStageAsTextRect.y))
        
        
    def drawTimer(self, start_ticks):
        font = pygame.font.SysFont(None, 48)
        timer = (pygame.time.get_ticks() - start_ticks) / 1000 
        # Create Text
        textTimer = font.render(str(int(timer)), True, Background.BLACK_COLOR)
        tTimerRect = textTimer.get_rect()
        tTimerRect.x = Background.SCREEN_WIDTH - 50
        tTimerRect.y = 50
        self.screen.blit(textTimer, (tTimerRect.x, tTimerRect.y))
