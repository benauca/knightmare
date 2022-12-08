import time
import pygame
from pygame.locals import *

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 600
FPS = 60
TEXT_PULSE_SPACE_TO_START = 'Pulse Space Key!'
TEXT_START_GAME = 'Start Game'
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Knightmare!")

clock = pygame.time.Clock()

running = True
SPEED_X = 1
SPEED = .05

font = pygame.font.SysFont(None, 36)


textPulse = font.render(TEXT_PULSE_SPACE_TO_START,
                        False, pygame.Color("white"))

tRect = textPulse.get_rect()
tRect.x = SCREEN_WIDTH / 2
tRect.y = SCREEN_WIDTH / 2

colors = []
current_color = 0
colors.append(pygame.Color("white"))
colors.append(pygame.Color("black"))

while running:
    
    # keep loop running at the right speed
    clock.tick(FPS)

    # Process input (events)
    events = pygame.event.get()
   
    '''tRect.x = tRect.x - SPEED_X'''
    # Rellenamos la pantalla antes de pintar el texto en movimiento.
    screen.fill(pygame.Color("black"))
    #Aplicamos el color al texto
    current_color += SPEED
    if current_color >= len(colors):
        current_color = 0
        
    textPulse = font.render(TEXT_PULSE_SPACE_TO_START,
                        False, colors[int(current_color)])
                        
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                textPulse = font.render(TEXT_START_GAME, False, colors[int(current_color)])
                screen.blit(textPulse, (tRect.x, tRect.y))
                pygame.display.flip()            
                time.sleep(3)
                running = False
    screen.blit(textPulse, (tRect.x, tRect.y))
    pygame.display.flip()
    

