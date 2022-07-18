from os import path

class Background:
    img_dir = path.join(path.dirname(__file__), 'assets')

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 480
    FPS = 60

    # define colors
    WHITE_COLOR = (255, 255, 255)
    BLACK_COLOR = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    def __init__(self) -> None:
        pass