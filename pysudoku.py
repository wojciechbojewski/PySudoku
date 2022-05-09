import pygame

from PyGameSudoku.Colors import Colors
from PyGameSudoku.ButtonClass import ButtonClass
from PyGameSudoku.Parameters import *

def game():
    pygame.init()
    pygame.display.set_caption(Config.title)
    screen = pygame.display.set_mode((Config.shape.width, Config.shape.height), 0, 32)
    screen.fill(Colors.white)
    for btn in ButtonItems:
        btn.draw(screen)
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
    quit()

if __name__ == "__main__":
    game()
