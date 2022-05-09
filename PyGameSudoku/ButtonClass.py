from PyGameSudoku.Colors import Colors

class ButtonClass:
    def __init__(self, id):
        self._id = id
        self.label = ""
        self.enable = 0
        self.visible = 0
        self.coordination = { "x" : 0, "y" : 0}
        self.size = { "width" : 0, "height" : 0}
        self.color = "white"
        self.background = "white"

    def draw(self, screen):
        import pygame
        pygame.draw.rect(screen, getattr(Colors, self.background), (self.coordination["x"], self.coordination["y"], self.size["width"], self.size["height"]))
        defaultFont = pygame.font.SysFont("Cambria", 72)
        tekst = defaultFont.render(self.label, False,  getattr(Colors, self.color) , getattr(Colors, self.background) )
        tekst = pygame.transform.scale(tekst, (self.size["width"]*0.90, self.size["height"]*0.99))
        ramka = tekst.get_rect()
        ramka.centerx = self.coordination["x"]+self.size["width"]//2
        ramka.centery = self.coordination["y"]+self.size["height"]//2
        screen.blit(tekst, ramka)
        pygame.display.update( (self.coordination["x"], self.coordination["y"], self.size["width"], self.size["height"])  )


    def update(self, dc):
        self.label = dc.label
        self.enable = dc.enable
        self.visible = dc.visible
        self.coordination = { "x" : dc.coordination.x, "y" : dc.coordination.y}
        self.size = { "width" : dc.size.width, "height" : dc.size.height}
        self.color = dc.color
        self.background = dc.background
        pass