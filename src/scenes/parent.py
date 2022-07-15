import pygame
from background import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, img_dir, WHITE_COLOR
from os import path

class ParentScene:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Knightmare!")
        pygame.display.set_icon(pygame.image.load(path.join(img_dir,'player.png')).convert())
        self.clock = pygame.time.Clock()
        

