# tetris.py
#  Classic tetris game written with Pythons Pygame Library
#  Author: Kyle Pollina


import pygame
import random
from board import Board
from board import Block
from definitions import *


##############################
# game_loop() - code for running the game loop
# 
##############################
def game_loop():
    global running
    running = True

    while running:
        # DO NOT EDIT
        clock.tick(FPS)     # keeps the game running at the right speed
        process_input()     # processes user input
        update()            # processes anything that needs to be updated every tick
        draw()              # draws the screen


##############################
# update() - this is the meat and potatoes of the games code
#  if you want to update game pieces, do it here
##############################
def update():
    # TODO remove dummy code
    i = 0


##############################
# process_input() - processes all user input
#
##############################
def process_input():
    events = pygame.event.get()
    for event in events:
        #check for closing the window
        if event.type == pygame.QUIT:
            global running
            running = False
            

##############################
# game_setup() - setting up the actual game
#
##############################
def game_setup():
    global all_sprites  # list of all sprites currently existing
    global board        # 2D board array 10x20
    global cur_block    # current falling block
    global next_block   # next block
    global hold_block   # hold block

    all_sprites = pygame.sprite.Group()
    board = Board(10, 20)
    nextboard = Board(4, 4)
    holdboard = Board(4, 4)
    cur_block = rand_block()  

    # board.print_array()

# creates and returns a random block
def rand_block():
    return Block(random.randint(0,6))


# ---------------------------------------

##############################
# run() - code to execute the game
#  run() is called way down at the bottom of the file
##############################
def run():
    pygame_setup()
    game_setup()
    game_loop()
    pygame.quit()




##############################
# pygame_setup() - setting up the pygame environment
#  probably shouldn't change anything here other than font
##############################
def pygame_setup():
    global screen       # screen object of size WIDTH x HEIGHT
    global font         # font type
    global clock        # game clock

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption(TITLE)
    pygame.font.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont(None, 20)
    clock = pygame.time.Clock()


##############################
# draw() - draws objects on the screen. 
#
##############################
def draw():
    # DO NOT EDIT
    pygame.display.flip()
    
    # EDIT HERE
    global board
    global nextBlock

    all_sprites.draw(screen) 
    screen.fill(BLACK)
    render_text('NEXT', WHITE, BLACK, BOARDRIGHT + 35, BOARDTOP - 20)
    pygame.draw.rect(screen, WHITE, (BOARDLEFT - 2, BOARDTOP - 2, BOARDWIDTH + 2, BOARDHEIGHT + 2), 1)

    # draws the board at the x, y coordinate
    for col in range(board.width):
        for row in range(board.height):
            if board.array[row][col] == -1:
                pygame.draw.rect(screen, WHITE, (BOARDLEFT + 20 * col, BOARDTOP + 20 * row, 18, 18), 1)
 

##############################
# render_text() - render text on the screen
# 
##############################
def render_text(string, fontcolor, bgcolor, x, y):
    textsurface = font.render(string, True, fontcolor, bgcolor)
    screen.blit(textsurface, (x,y))



##############################
# Start program
##############################
run()


