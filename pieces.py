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

    i = [[(0,1),(1,1),(2,1),(3,1)],[(1,0),(1,1),(1,2),(1,3)]]

    def __init__(self,x,y,rotation,shape,color):
        super().__init__()
        self.image = pygame.Surface([Screen.blockWidth * 4,Screen.blockWidth * 4])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.x, self.y = x,y
        self.rect = self.image.get_rect()
        self.color = color
        self.rotation = rotation
        self.draw()

        """if shape == "I":
            self.shape = self.I
            print("Generating an I piece")
        elif shape == "J":
            pass
        else:
            pass
        self.rotation = rotation
        self.color = color"""
    def rotate(self):
        self.rotation = (self.rotation + 1) % 3

    def draw(self):
        for val in self.i[self.rotation]:
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