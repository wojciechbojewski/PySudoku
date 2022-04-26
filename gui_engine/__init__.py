import pygame

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
        if (self._x) <= x <= (self._x)+23*len(self._label)+10 and (self._y) <= y <= (self._y)+55:
            return 1
        return 0