
#import Engine as se
import pygame
from Gui.TButton import TButton
from Gui.Config import GameParameters

items = []
gp = GameParameters()
for item in gp.Config["items"]:
    if gp.Config["items"][item]["type"] == "button":
            items.append( TButton().enable(gp.Config["items"][item]["enable"])\
                                   .label(gp.Config["items"][item]["label"])\
                                   .position(gp.Config["items"][item]["xy"]["x"], gp.Config["items"][item]["xy"]["y"])\
                                   .visible(gp.Config["items"][item]["visible"])
                                   )

pygame.init()
pygame.display.set_caption(gp.Config["title"])
screen = pygame.display.set_mode((gp.Config["shape"]["width"], gp.Config["shape"]["height"]))
picture = pygame.image.load(gp.Config["background"])
screen.blit(pygame.transform.scale(picture, (gp.Config["shape"]["width"], gp.Config["shape"]["height"])), (0, 0))

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

