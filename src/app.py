import pygame
from pygame.locals import *
from background import Background
from os import path
from parent import *
from initScene import *
from startScene import *
from levelOneScene import *


class App:
    """Create a single-window app with multiple scenes."""

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(
            (Background.SCREEN_WIDTH, Background.SCREEN_HEIGHT)
        )
        # Game loop

        pygame.display.set_caption("Knightmare!")
        pygame.display.set_icon(
            pygame.image.load(path.join(Background.img_dir, "player.png")).convert()
        )

        self.clock = pygame.time.Clock()
        self.currentScene = None
        self.scenes = {}

    def run(self, initial_scene, fps=Background.FPS):
        """Run the main event loop."""
        self.currentScene = self.scenes[initial_scene]
        self.running = True

        while self.running:
            pygame.time.get_ticks()
            # keep loop running at the right speed
            self.clock.tick(fps)
            # Process input (events)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            self.currentScene.processEvents(events)
            self.currentScene.run()
            self.currentScene.draw(self.screen)
            self.changeScene(self.currentScene)

            if self.running:
                self.running = self.currentScene.running

            pygame.display.flip()

        # time.sleep(3)

    def changeScene(self, currentScene):
        if currentScene.nextScene:
            if currentScene.toScene not in self.scenes:
                self.addScene(currentScene.toScene)
            self.currentScene = self.scenes[currentScene.toScene]

    def addScene(self, sceneName):
        className = sceneName + "Scene"
        sceneObj = globals()[className]
        self.scenes[sceneName] = sceneObj()


if __name__ == "__main__":
    app = App()
    app.addScene("Init")
    app.run(initial_scene="Init")
