import pygame
import random
from screen import Screen

class Piece:
    I = [[0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]]

    YELLOW = (255,255,0)
    shapes = [I]
    def __init__(self,x,y,rotation,shape,color):
        self.x, self.y = x,y
        self.rect = pygame.Rect(x,y,Screen.blockWidth,Screen.blockWidth)
        if shape == "I":
            self.shape = self.I
            print("Generating an I piece")
        elif shape == "J":
            pass
        else:
            pass
        self.rotation = rotation
        self.color = color

    def draw(self,surface):
        for x in range(len(self.shape[self.rotation])):
            print(self.shape[self.rotation][x])
            """if self.shape[self.rotation][x] == 1:
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