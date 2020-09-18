#import and initialize the pygame library
import pygame
from screen import Screen
from pieces import Piece
pygame.init()

# This implementation is based on this tutorial
# https://gamedevelopment.tutsplus.com/tutorials/implementing-tetris-collision-detection--gamedev-852


def print_board():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print(" ")

#The board will be a  10x 16 multi-dimensional array
board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

print_board()

#set up the drawing window
screen = pygame.display.set_mode([Screen.getScreenWidth(),Screen.getScreenHeight()])

YELLOW = (255,255,0)
rotate = False
iPiece = Piece(50,50,3,"I",YELLOW)
spriteList = pygame.sprite.Group()
spriteList.add(iPiece)
gameIsRunning = True
while gameIsRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rotate = True


    screen.fill((255,255,255))
    # Draw a solid blue circle in the center

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    for x in range(0,12):
        pygame.draw.line(screen,pygame.Color(255,145,110),(0,x * 15),(100, x * 15),5)

    if rotate == True:
        spriteList.update()
        rotate = False

    spriteList.draw(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()