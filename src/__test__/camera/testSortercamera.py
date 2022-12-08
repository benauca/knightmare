import pygame, sys
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
    '''Funcionalidad de la camara. Ordenacion de elementos según eje y, y demás'''
    def __init__(self) -> None:
        super().__init__()
        # vamos a crear un dislay_surface donde dibujar los elementos y así no necesitar el elemento screen
        self.display_surface = pygame.display.get_surface()
        self.ground_surf = pygame.image.load('assets/ground.png').convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft= (0,0))
    
    def custom_draw(self):
        # Ground
        self.display_surface.blit(self.ground_surf, self.ground_rect)
        # active elements
        # Ordenamos los items en funcion del eje Y para que siempre esten visibiles los elementos con Mayor Y
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            self.display_surface.blit(sprite.image, sprite.rect)

    
## Inicializamos el test
pygame.init()

# Establecemos el tamaño de la pantalla
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Incializamos la camara como un nuevo sprite
camera_group=CameraGroup()
# Incializamos el jugador dentro del  group camera_group en la posicion (640, 360) 
Player((640, 360), camera_group)

# Creamos de manera aleatoria de algunos arboles dentro del mapa
for i in range(20):
    random_x = randint(0, 1000)
    random_y = randint(0, 1000)
    Tree((random_x, random_y), camera_group)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(pygame.Color("white"))

    camera_group.update()
    camera_group.custom_draw()

    pygame.display.update()
    clock.tick(60)

