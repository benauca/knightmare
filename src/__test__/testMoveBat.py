from cgi import test
import time
import pygame
from pygame.locals import *

class TestMoveBat:
    
    SCREEN_WIDTH = 480
    SCREEN_HEIGHT = 600
    FPS = 60

    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Test!")
        self.clock = pygame.time.Clock()
        self.running = True


        self.x_pos = self.SCREEN_WIDTH / 3
        self.y_pos = 5

        self.y_speed = 1
        self.x_speed = -3
        self.gravity_y = 10 # Depending on how fast you want gravity to be

    def run(self):

        while self.running:
    
            # keep loop running at the right speed
            self.clock.tick(self.FPS)
                
            if self.x_pos >= self.SCREEN_WIDTH - 20 or self.x_pos <= 10:
                self.x_speed *= -1
                self.y_pos += self.gravity_y
                
            self.x_pos += self.x_speed
            self.y_pos += self.y_speed

            
            self.screen.fill(pygame.Color("white"))
            pygame.draw.rect(self.screen, pygame.Color("black"), (self.x_pos, self.y_pos, 10, 10))
            pygame.display.update()
            
            # Process input (events)
            events = pygame.event.get()
        
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()
            

NUMBER_BATS = 5
current_bats = 0

startTime = time.time()
if current_bats <= NUMBER_BATS:
    testMove = TestMoveBat()
    testMove.run()
    current_bats +=1
    time.sleep(1.0 - ((time.time() - startTime) % 1))

