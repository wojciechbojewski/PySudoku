import pygame

class Application:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((640, 480), 0, 32)

    def setCaption(self, title):
        pygame.display.set_caption(title)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    running = False
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pygame.quit()
        quit()
