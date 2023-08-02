import pygame
from board import boards

pygame.init()

#Global variables for h * w
WIDTH = 900
HEIGHT = 950

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
active_level = 0
level = boards[active_level]

run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    draw_board()

    #condition to exit the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #
    pygame.display.flip()
pygame.quit()
