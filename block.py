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

UP          = 0
RIGHT       = 1
DOWN        = 2
LEFT        = 3

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


##############################
# Classes 
##############################


# Individual square pieces that make up a block
class Square(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = (BOARDLEFT, BOARDTOP)

        pygame.draw.rect(self.image, color, (1, 1, 18, 18), 0)

# Full block made up of 4 squares
class Block:

    def __init__(self, block_type):
        self.color = BLACK
        self.squares = [0, 0, 0, 0]
        self.block_type = block_type
        self.dir = UP
        
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

        self.squares[0] = self.square1
        self.squares[1] = self.square2
        self.squares[2] = self.square3
        self.squares[3] = self.square4



    def check_collide(self, deadsquares):
        if self.get_bottom() >= BOARDBOT:
            return True
            
        for square in self.squares:
            for dead in deadsquares.deadsquare_list:
                if square.rect.y + 20 == dead.rect.y and square.rect.x == dead.rect.x:
                    return True

        return False
   
    def rotate_right(self):
        self.dir += 1
        self.dir = self.dir % 4

        if self.block_type == LINE:
            if self.dir == UP:
                self.squares[0].rect.x += 20
                self.squares[0].rect.y -= 20
                self.squares[2].rect.x -= 20
                self.squares[2].rect.y += 20
                self.squares[3].rect.x -= 40
                self.squares[3].rect.y += 40
            if self.dir == RIGHT:
                self.squares[0].rect.x -= 20
                self.squares[0].rect.y += 20
                self.squares[2].rect.x += 20
                self.squares[2].rect.y -= 20
                self.squares[3].rect.x += 40
                self.squares[3].rect.y -= 40
            if self.dir == DOWN:
                self.squares[0].rect.x += 20
                self.squares[0].rect.y -= 20
                self.squares[2].rect.x -= 20
                self.squares[2].rect.y += 20
                self.squares[3].rect.x -= 40
                self.squares[3].rect.y += 40
            if self.dir == LEFT:
                self.squares[0].rect.x -= 20
                self.squares[0].rect.y += 20
                self.squares[2].rect.x += 20
                self.squares[2].rect.y -= 20
                self.squares[3].rect.x += 40
                self.squares[3].rect.y -= 40


            
            
            
    def rotate_left(self):
        self.dir -= 1
        if self.dir == 0:
            self.dir = 4
        self.dir = self.dir % 4

        if self.block_type == LINE:
            if self.dir == UP:
                self.squares[0].rect.x += 20
                self.squares[0].rect.y -= 20
                self.squares[2].rect.x -= 20
                self.squares[2].rect.y += 20
                self.squares[3].rect.x -= 40
                self.squares[3].rect.y += 40
            if self.dir == RIGHT:
                self.squares[0].rect.x -= 20
                self.squares[0].rect.y += 20
                self.squares[2].rect.x += 20
                self.squares[2].rect.y -= 20
                self.squares[3].rect.x += 40
                self.squares[3].rect.y -= 40
            if self.dir == DOWN:
                self.squares[0].rect.x += 20
                self.squares[0].rect.y -= 20
                self.squares[2].rect.x -= 20
                self.squares[2].rect.y += 20
                self.squares[3].rect.x -= 40
                self.squares[3].rect.y += 40
            if self.dir == LEFT:
                self.squares[0].rect.x -= 20
                self.squares[0].rect.y += 20
                self.squares[2].rect.x += 20
                self.squares[2].rect.y -= 20
                self.squares[3].rect.x += 40
                self.squares[3].rect.y -= 40



    def set_next(self):
        for square in self.squares:
            square.rect.x += BOARDWIDTH + 20 

            if self.block_type == LINE:
                square.rect.x += 25
                square.rect.y += 5
            elif self.block_type == SQUARE:
                square.rect.x += 15
                square.rect.y += 25
            elif self.block_type == TBLOCK:
                square.rect.x += 15
                square.rect.y += 15
            else:
                square.rect.x += 5
                square.rect.y += 25

    def set_current(self):
        for square in self.squares:
            if self.block_type == LINE:
                square.rect.x -= 25
                square.rect.y -= 5
            elif self.block_type == SQUARE:
                square.rect.x -= 15
                square.rect.y -= 25
            elif self.block_type == TBLOCK:
                square.rect.x -= 15
                square.rect.y -= 15
            else:
                square.rect.x -= 5
                square.rect.y -= 25

            square.rect.x -= (BOARDWIDTH / 2) + 40

    def display(self, all_sprites):
        for square in self.squares:
            all_sprites.add(square)
    
    def move_down(self):
        if self.get_bottom() < BOARDBOT:
            for square in self.squares:
                square.rect.top += 20

    def fast_move(self, deadsquares):
        while not self.check_collide(deadsquares):
            for square in self.squares:
                square.rect.y += 20

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
    

# All squares/blocks that have collided
class Deadsquares:
    deadsquare_list = []

    def add_block(self, block):
        for square in block.squares:
            self.deadsquare_list.append(square)


