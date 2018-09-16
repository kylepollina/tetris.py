# tetris.py
#  Classic tetris game written with Pythons Pygame Library
#  Author: Kyle Pollina

import pygame
import random
from definitions import *

# code to run the program
def run():
    pygame_setup()
    game_loop()
    pygame.quit()


# game loop
def game_loop():
    global running
    running = True

    while running:
        # keep loop running at the right speed
        clock.tick(FPS)

        process_input()
        # update
        draw()


# processes all user input
def process_input():
    events = pygame.event.get()
    for event in events:
        #check for closing the window
        if event.type == pygame.QUIT:
            global running
            running = False
            

# draw / render
def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (BOARDLEFT - 2, BOARDTOP - 2, BOARDWIDTH + 4, BOARDHEIGHT + 4), 1)
    pygame.draw.rect(screen, WHITE, (BOARDRIGHT + 18, BOARDTOP - 2, 74, 94), 1)
    all_sprites.draw(screen) 
    render_text('NEXT', WHITE, BLACK, BOARDRIGHT + 35, BOARDTOP - 20)

    # After drawing everything, flip the display
    pygame.display.flip()


# setting up pygame environment
def pygame_setup():
    global screen
    global font
    global clock
    global all_sprites

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption(TITLE)
    pygame.font.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont(None, 20)
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()

 
# render text on the screen
def render_text(string, color, bgcolor, x, y):
    textsurface = font.render(string, True, color, bgcolor)
    screen.blit(textsurface, (x,y))



##############################
# Start program
##############################
run()
