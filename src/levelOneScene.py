from background import Background
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
    bats = []
    NUMBER_BATS = 5
    current_bats = 0
    time_elapsed_since_last_action = 0

    # Datos de puntuación

    score = 0
    lifes = 3
    level = 1

    def __init__(self) -> None:
        ParentScene.__init__(self)
        self.clock = pygame.time.Clock()
        self.running = True
        self.nextScene = False

        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.player = Player()
        # self.monster = Monster()

        # self.all_sprites.add(self.monster)

    '''Scene Loop'''

    def run(self) -> None:
        super().run()
        if self.current_bats < self.NUMBER_BATS:
            dt = self.clock.tick()
            self.time_elapsed_since_last_action += dt

            if self.time_elapsed_since_last_action > 1:
                bat = Bat()
                self.bats.append(bat)
                self.all_sprites.add(bat)
                self.current_bats += 1
                self.time_elapsed_since_last_action = 0

        for bullet in self.player.bullets:
            for bat in self.bats:

                if bat.rect.colliderect(bullet.rect):
                    bullet.kill()
                    self.all_sprites.remove(bullet)
                    Bullet.number_bullets = Bullet.number_bullets - 1
                    bat.remove(self.all_sprites)
                    self.current_bats -= 1

        for bat in self.bats:
            if bat.y_pos >= Background.SCREEN_HEIGHT:  # and self.current_bats >= 0:
                bat.x_pos = bat.y_pos = bat.SPEED_X = bat.SPEED_Y = bat.gravity_y = 0
                bat.remove(self.all_sprites)
                self.current_bats -= 1
                print("later: currents_bats", self.current_bats)

        # Update
        self.all_sprites.update()
        self.player.animate(0.15)
        # self.monster.animate(0.15)
        for bat in self.bats:
            bat.animate(0.15)

    def draw(self, screen) -> None:

        self.all_sprites.draw(screen)
        self.all_sprites.add(self.player)

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
