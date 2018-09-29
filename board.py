# board.py
#  board class for tetris.py
#  Author: Kyle Pollina

from definitions import *

FALL = 0
WAIT = 1
HOLD = 2

# class for the grid/array of the board
class Board:
    def __init__(self, width, height):
        self.array  = [[-1 for x in range(width)] for y in range(height)]
        self.width = width
        self.height = height
        self.blocks = []    # list of all blocks on the board

    # draws the board at the x, y coordinate
    def draw(self, x, y, pygame):
        for col in range(self.width):
            for row in range(self.height):
                if self.array[row][col] == -1:
                    pygame.draw.rect(screen, WHITE, (x + 20 * col, y + 20 * row, 18, 18), 1)



    def print_array(self):
        for x in self.array:
            for y in x:
                print(y, end=' ')
            print("\n")


class Block:
    def __init__(self, type):
        self.type = type
        self.square1 = (-1,-1)
        self.square2 = (-1,-1)
        self.square3 = (-1,-1)
        self.square4 = (-1,-1)


