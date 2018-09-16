# tetris.py
#  Classic tetris game written with Pythons Pygame Library
#  Author: Kyle Pollina

import pygame
import random
from definitions import *

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
# game_loop() - code for running the game loop
# 
##############################
def game_loop():
    global running
    running = True

    while running:
        # DO NOT EDIT
        clock.tick(FPS)     # keeps the game running at the right speed
        process_input()
        # update
        draw()

        


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
# draw() - draws objects on the screen. 
#
##############################
def draw():
    # DO NOT EDIT
    pygame.display.flip()
    
    # EDIT HERE
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (BOARDLEFT - 2, BOARDTOP - 2, BOARDWIDTH + 4, BOARDHEIGHT + 4), 1)
    pygame.draw.rect(screen, WHITE, (BOARDRIGHT + 18, BOARDTOP - 2, 74, 94), 1)
    render_text('NEXT', WHITE, BLACK, BOARDRIGHT + 35, BOARDTOP - 20)
    all_sprites.draw(screen) 



##############################
# game_setup() - setting up the actual game
#
##############################
def game_setup():
    global all_sprites  # list of all sprites currently existing

    all_sprites = pygame.sprite.Group()


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
# render_text() - render text on the screen
#  string  - the string of the text you wish to render
#  color   - the color of the font
#  bgcolor - the background color of the text
#  x - x coordinate
#  y - y coordinate
##############################
def render_text(string, color, bgcolor, x, y):
    textsurface = font.render(string, True, color, bgcolor)
    screen.blit(textsurface, (x,y))



##############################
# Start program
##############################
run()


