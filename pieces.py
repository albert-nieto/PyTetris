import pygame
import random
from screen import Screen

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

class Piece(pygame.sprite.Sprite):
    """
    This class represents a tetris piece.
    """
    I = [[0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]]

    i = [[(0,1),(1,1),(2,1),(3,1)],[(2,0),(2,1),(2,2),(2,3)],[(0,2),(1,2),(2,2),(3,2)],[(1,0),(1,1),(1,2),(1,3)]]
    J = [[(1,0),(1,1),(1,2),(0,2)],[(0,0),(0,1),(1,1),(2,1)],[(1,0),(2,0),(1,1),(1,2)],[(0,1),(1,1),(2,1),(2,2)]]
    L = [[(1,0),(1,1),(1,2),(2,2)],[(0,2),(0,1),(1,1),(2,1)],[(1,0),(0,0),(1,1),(1,2)],[(0,1),(1,1),(2,1),(2,0)]]
    O = [[(0,0),(1,0),(0,1),(1,1)],[(0,0),(1,0),(0,1),(1,1)],[(0,0),(1,0),(0,1),(1,1)],[(0,0),(1,0),(0,1),(1,1)]]
    S = [[(0,2),(1,1),(1,2),(2,1)],[(0,0),(0,1),(1,1),(1,2)],[(0,1),(1,0),(1,1),(2,0)],[(1,0),(1,1),(2,1),(2,2)]]
    T = [[(0,1),(1,1),(2,1),(1,2)],[(1,0),(1,1),(1,2),(0,1)],[(1,0),(0,1),(1,1),(2,1)],[(1,0),(1,1),(1,2),(2,1)]]
    Z = [[(0,1),(1,1),(1,2),(2,2)],[(1,0),(1,1),(0,2),(0,1)],[(0,0),(1,0),(1,1),(2,1)],[(2,0),(2,1),(1,1),(1,2)]]

    def __init__(self,x,y,rotation,shape,color):
        super().__init__()
        self.image = pygame.Surface([Screen.blockWidth * 4,Screen.blockWidth * 4])
        #self.image.fill(RED)
        self.image.set_colorkey(WHITE)
        self.x, self.y = x,y
        self.rect = self.image.get_rect()
        pygame.Rect.move_ip(self.rect, x, y)
        self.color = color
        self.rotation = rotation

        if shape == "i":
            self.shape = self.i
            print("Generating an I piece")
        elif shape == "J":
            self.shape = self.J
        elif shape == "L":
            self.shape = self.L
        elif shape == "O":
            self.shape = self.O
        elif shape == "S":
            self.shape = self.S
        elif shape == "T":
            self.shape = self.T
        elif shape == "Z":
            self.shape = self.Z
        else:
            pass

        self.draw()

    def update(self, rot):
        print("moving")
        self.y += Screen.blockWidth
        self.rect = self.image.get_rect()
        pygame.Rect.move_ip(self.rect, self.x , self.y)
        if rot == True:
            self.rotate()

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4
        print("update was called" + str(self.rotation))
        self.draw()

    def draw(self):
        print("Draw called")
        self.image.fill(WHITE)
        for val in self.shape[self.rotation]:
            pygame.draw.rect(self.image, self.color, [val[0] *Screen.blockWidth, val[1]*Screen.blockWidth, Screen.blockWidth, Screen.blockWidth])


        """for x in range(len(self.shape[self.rotation])):
            print(self.shape[self.rotation][x])
            if self.shape[self.rotation][x] == 1:
                pygame.draw.rect(surface,self.color,self.rect)
            self.rect.x += Screen.blockWidth
            if (x > 1) and (x % 3) == 0:
                self.rect.y += Screen.blockWidth
                self.rect.x = self.x"""
        pass

"""def toBinString(hex_data):
    return bin(int(hex_data, 16))[2:].zfill(16)
I = ["0x0F00", "0x2222", "0x00F0", "0x4444"]
i = [[0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],
     [0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0],[0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0],[YELLOW]]

print(toBinString(I[0]))
print(i[0])

for x in i:
    for y in x:
        print(str(y), end= " ")
    print()
"""