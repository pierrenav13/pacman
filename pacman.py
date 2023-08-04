import pygame
from board import boards
import math

pygame.init()

#Global variables for h * w
#Dimensions and powerup size multiplied by .8 for personal screen size
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
player_images = []
#using *.8 for personal screen size
for i in range(1, 5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (38, 38)))
player_x = 335
player_y = 520
direction = 0
counter = 0
flicker = False

def draw_board():
    #height and width of each tile/piece
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)
    #iterate through each row in the level
    for i in range(len(level)):
        #iterate through each column for the row 
        for j in range(len(level[i])):
            #1 small circle, 2 powerup
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5*num2), i * num1 + (0.5 * num1)), 4 * .8)
            if level[i][j] == 2 and not flicker:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5*num2), i * num1 + (0.5 * num1)), 10 * .8)
            #3 Vertical, 4 Horizontal
            if level[i][j] == 3:
                pygame.draw.line(screen, color, ((j * num2 + (0.5*num2), i * num1)),  (j * num2 + (0.5*num2), i * num1 + num1), 3)
            if level[i][j] == 4:
                pygame.draw.line(screen, color, ((j * num2, (0.5*num1) + i * num1)),  (j * num2 + num2, i * num1 + (0.5*num1)), 3)
            #5-8 Corners, 9 Ghost Gate
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j*num2 - (num2*0.4)) - 2, (i * num1 + (0.5*num1)), num2, num1], 0, PI/2, 3)
            if level[i][j] == 6:
                pygame.draw.arc(screen, color, [(j*num2 + (num2*0.5)), (i * num1 + (0.5*num1)), num2, num1], PI/2, PI, 3)
            if level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j*num2 + (num2*0.5)), (i * num1 - (0.4*num1)), num2, num1], PI, (3*PI)/2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(screen, color, [(j*num2 - (num2*0.4)) - 2, (i * num1 - (0.4*num1)), num2, num1], (3*PI)/2, (2*PI), 3)
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', ((j * num2, (0.5*num1) + i * num1)),  (j * num2 + num2, i * num1 + (0.5*num1)), 3)

def draw_player():
    #Right-0, Left-1, Up-2, Down-3
    if direction == 0:
        screen.blit(player_images[counter // 5], (player_x, player_y))
    if direction == 1:
        screen.blit(pygame.transform.flip(player_images[counter // 5], True, False), (player_x, player_y))
    if direction == 2:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
    if direction == 3:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 270), (player_x, player_y))
    

run = True
while run:
    timer.tick(fps)
    if counter < 19:
        counter += 1
        if counter > 7:
            flicker = False
    else:
        counter = 0
        flicker = True

    screen.fill('black')
    draw_board()
    draw_player()
    center_x = player_x + 19
    center_y = player_y + 20
    pygame.draw.circle(screen, 'green', (center_x, center_y), 2)
    #check_position()

    #condition to exit the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == (pygame.K_d):
                direction = 0
            if event.key == (pygame.K_a):
                direction = 1
            if event.key == (pygame.K_w):
                direction = 2
            if event.key == (pygame.K_s):
                direction = 3

    pygame.display.flip()
pygame.quit()
