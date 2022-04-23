#import pygame
#pygame.init()
#screen = pygame.display.set_mode((640, 240))
#running = True
#while running:
#    for event in pygame.event.get():
#        print(event)
#        if event.type == pygame.QUIT:
#            running = False
#pygame.quit()

import sudoku_engine as se

sudoku = se.SudokuBoard("1ee24eeee/24e8e59e3/eee7e12e4/4e9158ee6/7e1ee9e4e/526eeee9e/e125eeeee/eeee37162/6eeeee5e8")
for item in sudoku.box(1, skipempty=True):
    print (item) 
