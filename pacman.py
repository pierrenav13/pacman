import pygame
from board import boards
import math

pygame.init()

#Global variables for h * w
WIDTH = 900 * .8
HEIGHT = 950 * .8

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
active_level = 0
level = boards[active_level]
color = 'blue'
PI = math.pi

def draw_board(l):
    #height and width of each tile/piece
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)
    #iterate through each row in the level
    for i in range(len(level)):
        #iterate through each column for the row 
        for j in range(len(level[i])):
            #1 small circle, 2 powerup
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5*num2), i * num1 + (0.5 * num1)), 4)
            if level[i][j] == 2:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5*num2), i * num1 + (0.5 * num1)), 10)
            if level[i][j] == 3:
                pygame.draw.line(screen, color, ((j * num2 + (0.5*num2), i * num1)),  (j * num2 + (0.5*num2), i * num1 + num1), 3)
            if level[i][j] == 4:
                pygame.draw.line(screen, color, ((j * num2, (0.5*num1) + i * num1)),  (j * num2 + num2, i * num1 + (0.5*num1)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j*num2 - (num2*0.4)) - 2, (i * num1 + (0.5*num1)), num2, num1], 0, PI/2, 3)
            
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', ((j * num2, (0.5*num1) + i * num1)),  (j * num2 + num2, i * num1 + (0.5*num1)), 3)


run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    draw_board(level)

    #condition to exit the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #
    pygame.display.flip()
pygame.quit()
