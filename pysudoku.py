
import sudoku_engine as se
import pygame
import json


class GameParameters(object):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameParameters, cls).__new__(cls)
        return cls._instance

class TButton():
    def __init__(self):
        self._enable = 0
        self._x = 0
        self._y = 0
        self._label = ""
        self._visible = 1
    
    def enable(self, e):
        self._enable = e
        return self

    def position(self, x, y):
        self._x = x
        self._y = y
        return self

    def label(self, l):
        self._label = l
        return self

    def visible(self, v):
        self._visible = v
        return self

    def draw(self, screen):
        font = pygame.font.SysFont('calibri.ttf', 50)
        img = font.render(self._label, True, (255,255,255)) 

        color = (255,0,0)
        if self._enable==0:
            color = (125,125,125)
        pygame.draw.rect(screen, color, (self._x,self._y,23*len(self._label)+10,55))
        screen.blit(img, (self._x+10, self._y+10))  

    def isactive(self, x, y):
        if (self._x) <= x <= (self._x)+23*len(self._label) and (self._y) <= y <= (self._y)+55:
            return 1
        return 0

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
            #pos = event.pos
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

