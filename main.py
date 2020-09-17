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

iPiece = Piece(50,50,0,"I",YELLOW)
gameIsRunning = True
while gameIsRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False

    screen.fill((255,255,255))
    # Draw a solid blue circle in the center

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    for x in range(0,12):
        pygame.draw.line(screen,pygame.Color(255,145,110),(0,x * 15),(100, x * 15),5)

    iPiece.draw(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()