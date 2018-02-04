#"Tetris" Tetris game made with Pygame
# Author: Kyle Pollina
import pygame
import random

# Define block types
SQUARE = 0
LINE   = 1
TBLOCK = 2
ZBLOCK = 3
SBLOCK = 4
JBLOCK = 5
LBLOCK = 6

# Define constants
WIDTH       = 20*20
HEIGHT      = 20*30
BOARDWIDTH  = 20*10
BOARDHEIGHT = 20*20
BOARDLEFT   = 5*20
BOARDRIGHT  = 15*20
BOARDTOP    = 5*20
BOARDBOT    = 25*20

# Define colors
WHITE  = (255,255,255)
BLACK  = (0,0,0)
RED    = (255,0,0)
GREEN  = (0,255,0)
BLUE   = (0,0,255)
YELLOW = (255,255,0)
CYAN   = (0,255,255)
PURPLE = (255,0,255)
ORANGE = (255,140,0)

# Classes
class Square(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = (BOARDLEFT, BOARDTOP)

        pygame.draw.rect(self.image, color, (1, 1, 18, 18), 0)


class Block:
    squares = []
    block_type = 0

    def __init__(self, block_type, all_sprites):
        
        self.color = BLACK
        
        if block_type == SQUARE:
            self.color = YELLOW
        if block_type == LINE:
            self.color = CYAN
        if block_type == TBLOCK:
            self.color = PURPLE
        if block_type == ZBLOCK:
            self.color = RED
        if block_type == SBLOCK:
            self.color = GREEN
        if block_type == LBLOCK:
            self.color = ORANGE
        if block_type == JBLOCK:
            self.color = BLUE
        
  
        self.square1 = Square(self.color)
        self.square2 = Square(self.color)
        self.square3 = Square(self.color)
        self.square4 = Square(self.color)

        if block_type == SQUARE:
            self.square2.rect.left += 20
            self.square3.rect.top  += 20
            self.square4.rect.left += 20
            self.square4.rect.top  += 20

        if block_type == LINE:
            self.square2.rect.top  += 20
            self.square3.rect.top  += 40
            self.square4.rect.top  += 60

        if block_type == TBLOCK:
            self.square2.rect.top  += 20
            self.square3.rect.top  += 20
            self.square3.rect.left += 20
            self.square4.rect.top  += 40
            
        if block_type == ZBLOCK:
            self.square2.rect.left  += 20
            self.square3.rect.top   += 20
            self.square3.rect.left  += 20
            self.square4.rect.top   += 20
            self.square4.rect.left  += 40
            
        if block_type == SBLOCK:
            self.square1.rect.top   += 20
            self.square2.rect.left  += 20
            self.square3.rect.top   += 20
            self.square3.rect.left  += 20
            self.square4.rect.left  += 40

        if block_type == JBLOCK:
            self.square2.rect.top   += 20
            self.square3.rect.top   += 20
            self.square3.rect.left  += 20
            self.square4.rect.top   += 20
            self.square4.rect.left  += 40

        if block_type == LBLOCK:
            self.square1.rect.top   += 20
            self.square2.rect.top   += 20
            self.square2.rect.left  += 40
            self.square3.rect.top   += 20
            self.square3.rect.left  += 20
            self.square4.rect.left  += 40

        self.squares.append(self.square1) 
        self.squares.append(self.square2) 
        self.squares.append(self.square3) 
        self.squares.append(self.square4) 

        all_sprites.add(self.square1, self.square2, self.square3, self.square4)



    def update(self):
        for square in self.squares:
            square.rect.top += 20

    def move_left(self):
        if self.get_left() > BOARDLEFT:
            for square in self.squares:
                square.rect.left -= 20

    def move_right(self):
        if self.get_right() < BOARDRIGHT:
            for square in self.squares:
                square.rect.left += 20


    # gets the farthest left block x value
    def get_left(self):
        self.left = self.squares[0].rect.left
        for square in self.squares:
            if square.rect.left <= self.left:
                self.left = square.rect.left

        return self.left
            

    # gets the farthest right block x value
    def get_right(self):
        self.right = self.squares[0].rect.right
        for square in self.squares:
            if square.rect.right >= self.right:
                self.right = square.rect.right

        return self.right

    # gets the lowest blocks bottom value
    def get_bottom(self):
        self.bottom = self.squares[0].rect.bottom
        for square in self.squares:
            if square.rect.bottom >= self.bottom:
                self.bottom = square.rect.bottom

        return self.bottom
    
