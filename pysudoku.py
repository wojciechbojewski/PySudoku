import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
quit()

