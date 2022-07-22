from background import Background
from parent import ParentScene
import pygame

from bullet import Bullet
from bat import Bat
from player import Player
from monster import Monster


'''number_bullets = 0'''
bullet_limit = 5

class LevelOneScene(ParentScene):

    NUMBER_BATS = 5
    NUMBER_MONSTER = 3
    current_bats = 0
    current_monsters = 0
    time_elapsed_since_last_action = 0

    # Datos de puntuación
    score = 0
    lifes = 3
    level = 1
    hi_score = 99999

    def __init__(self) -> None:
        ParentScene.__init__(self)
        self.clock = pygame.time.Clock()
        self.running = True
        self.nextScene = False

        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.bats = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()

        self.player = Player()
        self.start_ticks = pygame.time.get_ticks()
        self.flag = int(pygame.time.get_ticks() / 1000 )
        # self.monster = Monster()

    '''Scene Loop'''

    def run(self) -> None:
        super().run()
        ## Debo separar el metodo en draw y update. Afecta al time_elapsed_since_last_action
        self.drawScoreMenu()
        self.drawTimer(self.start_ticks)
        
        difference = (pygame.time.get_ticks() - self.start_ticks) / 1000
        if int(difference) % 10 == 0:
            if self.current_bats < self.NUMBER_BATS:
                dt = self.clock.tick()
                self.time_elapsed_since_last_action += dt
                if self.time_elapsed_since_last_action > 50:
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
                    self.score += 50
                    self.current_bats -= 1
                    self.current_monsters -=1
            for monster in self.monsters:
                if monster.rect.colliderect(bullet.rect):
                    bullet.kill()
                    monster.kill()
                    Bullet.number_bullets = Bullet.number_bullets - 1
                    self.score += 10

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
                self.lifes -= 1

        # Update
        self.all_sprites.update()
        self.player.animate(0.15)
        # self.monster.animate(0.15)
        for bat in self.bats:
            bat.animate(0.15)
        for monster in self.monsters:
            monster.animate(0.15)

    def draw(self, screen) -> None:
        self.all_sprites.draw(screen)
        self.all_sprites.add(self.player)


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

        scoreAsText = font.render(str(self.score), True, Background.WHITE_COLOR)
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

        hiScoreAsText = font.render(str(self.hi_score), True, Background.WHITE_COLOR)
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

        lifesAsText = font.render(str(self.lifes), True, Background.WHITE_COLOR)
        tLifesAsTextRect = lifesAsText.get_rect()
        tLifesAsTextRect.x = tScoreRect.x + Background.SCREEN_WIDTH / 2
        tLifesAsTextRect.y = tScoreRect.x + Background.SCREEN_HEIGHT - Background.SCREEN_HEIGHT / 4
        self.screen.blit(lifesAsText, (tLifesAsTextRect.x, tLifesAsTextRect.y))


        textStage = font.render("STAGE", True, Background.WHITE_COLOR)
        tStageRect = textStage.get_rect()
        tStageRect.x = tScoreRect.x + Background.SCREEN_WIDTH - Background.SCREEN_WIDTH / 4
        tStageRect.y = Background.SCREEN_HEIGHT - Background.SCREEN_HEIGHT / 4
        self.screen.blit(textStage, (tStageRect.x, tStageRect.y))

        stageAsText = font.render(str(self.level), True, Background.WHITE_COLOR)
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
