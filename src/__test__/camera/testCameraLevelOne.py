import pygame
import sys
from random import randint


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/tree.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 5


    def input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self):
        self.input()
        self.rect.center += self.direction * self.speed


class CameraGroup(pygame.sprite.Group):
    
    def __init__(self) -> None:
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0]/2
        self.half_y = self.display_surface.get_size()[1]/2

        self.ground_surf = pygame.image.load('assets/scene-01.png').convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))
    
    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_y

    def custom_draw(self, player):
        self.center_target_camera(player)
        groud_offset_pos = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf, groud_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

        #pygame.draw.rect(self.display_surface, pygame.Color('yellow'), self.camera_rect, 5)

    
# Inicializamos el test
pygame.init()

# Establecemos el tamaño de la pantalla
screen = pygame.display.set_mode((800, 480))
clock = pygame.time.Clock()

# Incializamos la camara como un nuevo sprite
camera_group = CameraGroup()
# Incializamos el jugador dentro del  group camera_group en la posicion (640, 360)
player = Player((400, 7900), camera_group)

# Creamos de manera aleatoria de algunos arboles dentro del mapa
for i in range(20):
    random_x = randint(0, 800)
    random_y = randint(0, 8000)
    Tree((random_x, random_y), camera_group)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pygame.Color("white"))

    camera_group.update()
    camera_group.custom_draw(player)

    pygame.display.update()
    clock.tick(60)
