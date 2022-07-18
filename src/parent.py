import pygame
from background import Background
from os import path


class ParentScene:
    """ Scene Parent"""

    HIGT_SCORE_TEXT = "HI SCORE"
    SCORE_TEXT = "SCORE"
    LIFE_TEXT = "REST"
    LEVEL_TEXT = "STAGE"

    def __init__(self) -> None:
        """Scene Init"""

        self.nextScene = False
        self.toScene = ""
        pygame.init()
        pygame.mixer.init()
        
        self.all_sprites = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((Background.SCREEN_WIDTH, Background.SCREEN_HEIGHT))
        pygame.display.set_caption("Knightmare!")
        pygame.display.set_icon(pygame.image.load(
            path.join(Background.img_dir, 'player.png')).convert())
        self.clock = pygame.time.Clock()


    def processEvents(self, events):
        """Procesa los eventos recibidos en la escena"""

    
    def run(self) -> None:
        """Se encarga de dibujar los elementos en la escena y la lógica de la misma"""
        pygame.time.get_ticks()
        # keep loop running at the right speed
        self.clock.tick(Background.FPS)
        self.screen.fill(Background.WHITE_COLOR)

    def draw(self, screen) -> None:
        """Pinta los elementos de la escena en la pantalla"""
        pass

