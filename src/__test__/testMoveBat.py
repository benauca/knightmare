import time
import pygame
from pygame.locals import *

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
class TestMoveBat:
    
    def __init__(self) -> None:
        self.running = True

        self.x_pos = SCREEN_WIDTH / 3
        self.y_pos = 5

        self.y_speed = 1
        self.x_speed = -3
        self.gravity_y = 10 # Depending on how fast you want gravity to be

    def run(self):
                    
        if self.x_pos >= SCREEN_WIDTH - 20 or self.x_pos <= 10:
            self.x_speed *= -1
            self.y_pos += self.gravity_y
            
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

    def __del__(self):
        print("kill bat")         
        self.x_speed = 0
        self.y_speed = 0
        self.x_pos = 0
        self.y_pos = 0
        self.gravity_y = 0


class HandlerTest:
    running = True
    NUMBER_BATS = 5
    current_bats = 0
    time_elapsed_since_last_action = 0
    def __init__(self) -> None:
        
        pygame.init()
        pygame.mixer.init()

        pygame.display.set_caption("Test!")
        self.clock = pygame.time.Clock()
        # keep loop running at the right speed

    def run(self):
        # keep loop running at the right speed
        bat = TestMoveBat()
        bats = []
        while self.running:

            if self.current_bats < self.NUMBER_BATS:
                dt = self.clock.tick()
                self.time_elapsed_since_last_action += dt
                if self.time_elapsed_since_last_action > 25:
                    bats.append(TestMoveBat())
                    self.current_bats +=1
                    # Reset to 0
                    self.time_elapsed_since_last_action = 0
            print("Before: current_bats", self.current_bats)
            self.clock.tick(FPS)
            screen.fill(pygame.Color("white"))
            pygame.draw.rect(screen, pygame.Color(
                "black"), (0, SCREEN_HEIGHT - SCREEN_HEIGHT / 4, SCREEN_WIDTH, SCREEN_HEIGHT / 4))
            for bat in bats:
                # Calculamos la posicion del murcielago  
                bat.run()
                # Pintamos el rectangulo en pantalla.
                pygame.draw.rect(screen, pygame.Color("black"), (bat.x_pos, bat.y_pos, 10, 10))

                if bat.y_pos > SCREEN_HEIGHT and self.current_bats >= 0:
                    bat.__del__()
                    self.current_bats -= 1
                    print("later: currents_bats", self.current_bats)
                    

            pygame.display.update()
            # Process input (events)
            events = pygame.event.get()
        
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()
            

handler = HandlerTest()
handler.run()
