
import sudoku_engine as se
import pygame
import json
from gui_engine import TButton

class GameParameters(object):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameParameters, cls).__new__(cls)
        return cls._instance

with open(".\\gui_engine\\main_board.json") as file:
		config = json.load(file)

items = []
for item in config["items"]:
    if config["items"][item]["type"] == "button":
            items.append( TButton().enable(config["items"][item]["enable"])\
                                   .label(config["items"][item]["label"])\
                                   .position(config["items"][item]["xy"]["x"], config["items"][item]["xy"]["y"])\
                                   .visible(config["items"][item]["visible"])
                                   )

pygame.init()
pygame.display.set_caption(config["title"])
screen = pygame.display.set_mode((config["shape"]["width"], config["shape"]["height"]))
picture = pygame.image.load(config["background"])
screen.blit(pygame.transform.scale(picture, (config["shape"]["width"], config["shape"]["height"])), (0, 0))

running = True
while running:
    screen.blit(picture, (0,0))
    for c in items:
        if c._visible:
            c.draw(screen)
 
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            for c in items:
                if c._visible:
                    if c.isactive(event.pos[0],event.pos[1]):
                        print(f"Clicked on {c._label}")

    pygame.display.update()

#fonts = pygame.font.get_fonts()
#print(len(fonts))
#for f in fonts:
#    print(f)

pygame.quit()
quit()

