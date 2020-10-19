import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

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
mainscreen = pygame.display.set_mode([Screen.getScreenWidth(),Screen.getScreenHeight()])

YELLOW = (255,255,0)
BLUE = (0,35,102)
rotate = False
iPiece = Piece(50,50,0,"i",YELLOW)
JPiece = Piece(300,300,0,"Z",BLUE)
spriteList = pygame.sprite.Group()
spriteList.add(iPiece)
spriteList.add(JPiece)

backImg = pygame.image.load('images/background.png')

gameIsRunning = True
clock = pygame.time.Clock()
FPS = 30
time_elapsed = 0
moveDown = False
while gameIsRunning:
    dt = clock.tick(FPS)
    time_elapsed += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rotate = True

    if time_elapsed >= 1000:
        #print((str(time_elapsed) + " has passed."))
        spriteList.update(rotate)
        time_elapsed = 0

    mainscreen.fill((255,255,255))

    mainscreen.blit(backImg,(Screen.screenWidth/2 - (150),Screen.screenHeight/2 -(240)))

    if rotate == True:
        spriteList.update(rotate)
        rotate = False

    spriteList.draw(mainscreen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()