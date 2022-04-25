
import sudoku_engine as se
import pygame
import json

with open(".\\gui_engine\\main_board.json") as file:
		config = json.load(file)

pygame.init()
pygame.display.set_caption(config["title"])
screen = pygame.display.set_mode((config["shape"]["width"], config["shape"]["height"]))
picture = pygame.image.load(config["background"])
screen.blit(pygame.transform.scale(picture, (config["shape"]["width"], config["shape"]["height"])), (0, 0))
pygame.display.flip()


def button(screen, label, enable, x, y ):
    font = pygame.font.SysFont('calibri.ttf', 50)
    img = font.render(label, True, (255,255,255)) 
    if enable=="1":
        pygame.draw.rect(screen, (255,0,0), (x-10,y-10,23*len(label)+10,55))
    else:
        pygame.draw.rect(screen, (125,125,125), (x-10,y-10,23*len(label)+10,55))
    screen.blit(img, (x, y))  
    return (label, x-10,y-10,23*len(label)+10, 55)     

running = True
while running:
    screen.blit(picture, (0,0))

    items = []
    for item in config["items"]:
        component = config["items"][item] 
        if component["type"] == "button":
            items.append(button(screen, component["label"], component["enable"], component["xy"]["x"] , component["xy"]["y"]))

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            print(pos)
            for item in items:
                if item[1] <= pos[0] <= item[1]+item[3] and item[2] <= pos[1] <= item[2]+item[4]:
                    print(f"Clicked on {item[0]}")

    pygame.display.update()


#fonts = pygame.font.get_fonts()
#print(len(fonts))
#for f in fonts:
#    print(f)

pygame.quit()
quit()

