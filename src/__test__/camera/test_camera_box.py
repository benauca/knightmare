""" Test for camera box"""
# Importamos los modulos necesarios

import sys
from random import randint
import pygame


class Tree(pygame.sprite.Sprite):
    """Clase para crear los arboles"""

    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("assets/tree.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


class Player(pygame.sprite.Sprite):
    """Clase para crear el jugador"""

    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self):
        """Gestionamos la entrada de teclado"""
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
        """Actualizamos la posicion del jugador en funcion de la direccion y la velocidad"""
        self.input()
        self.rect.center += self.direction * self.speed


class CameraGroup(pygame.sprite.Group):
    """
    Creamos una clase que hereda de pygame.sprite.Group para gestionar la camara.

    Funcionalidad de la camara. Ordenacion de elementos según eje y, y demás
    """

    def __init__(self) -> None:
        super().__init__()
        # Vamos a crear un dislay_surface donde dibujar los elementos y
        # un offset para gestionar la posicion de la camara
        # y no tener que mover todos los elementos de la pantalla

        self.display_surface = pygame.display.get_surface()

        # Offset asociado a la camara. Gestiona como se mueve la camara, que luego usaremos para
        # pintar en los # rectangulos de ground y de los sprites activos (Player and Tree)
        self.offset = pygame.math.Vector2()
        # POsition en X. Mitad del tamaño de la imagen
        # Posiction en Y. Mitad del tamaño de la imagen
        self.half_w = self.display_surface.get_size()[0] / 2
        self.half_y = self.display_surface.get_size()[1] / 2

        # Camera box
        self.camera_borders = {"left": 200, "right": 200, "top": 100, "bottom": 100}
        camera_left = self.camera_borders["left"]
        camera_top = self.camera_borders["top"]
        camera_weight = self.display_surface.get_size()[0] - (
            self.camera_borders["left"] + self.camera_borders["right"]
        )
        camera_height = self.display_surface.get_size()[1] - (
            self.camera_borders["top"] + self.camera_borders["bottom"]
        )

        self.camera_rect = pygame.Rect(
            camera_left, camera_top, camera_weight, camera_height
        )

        self.ground_surf = pygame.image.load("assets/ground.png").convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))

    """ Centra la camara en el target."""

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_y

    def box_target_camera(self, target):

        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom

        self.offset.x = self.camera_rect.left - self.camera_borders["left"]
        self.offset.y = self.camera_rect.top - self.camera_borders["top"]

    def custom_draw(self, player):
        # self.center_target_camera(player)
        self.box_target_camera(player)
        groud_offset_pos = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf, groud_offset_pos)

        # Active elements
        # Ordenamos los items en funcion del eje Y para que siempre esten visibiles los elementos
        # con Mayor Y
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):

            offset_pos = sprite.rect.topleft - self.offset
            # self.display_surface.blit(sprite.image, sprite.rect)
            # Pintaremos la imagen en funcion de la posicion de offset
            self.display_surface.blit(sprite.image, offset_pos)

        pygame.draw.rect(
            self.display_surface, pygame.Color("yellow"), self.camera_rect, 5
        )


# Inicializamos el test
pygame.init()

# Establecemos el tamaño de la pantalla
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Incializamos la camara como un nuevo sprite
camera_group = CameraGroup()
# Incializamos el jugador dentro del  group camera_group en la posicion (640, 360)
player = Player((640, 360), camera_group)

# Creamos de manera aleatoria de algunos arboles dentro del mapa
for i in range(20):
    random_x = randint(1000, 2000)
    random_y = randint(1000, 2000)
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
