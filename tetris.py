#"Tetris" Tetris game made with Pygame
# Author: Kyle Pollina
import pygame
import random
import copy
from block import Block
from block import Deadsquares

# Define constants
WIDTH       = 20*20
HEIGHT      = 20*30
BOARDWIDTH  = 20*10
BOARDHEIGHT = 20*20
BOARDLEFT   = 5*20
BOARDRIGHT  = 15*20
BOARDTOP    = 5*20
BOARDBOT    = 25*20
FPS         = 30

GAME_OVER = 0
RUN = 1
PAUSE = 2

TESTSPEED   = 10
NORMSPEED   = 20
SLOWSPEED   = 30

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

# Define block types
SQUARE = 0
LINE   = 1
TBLOCK = 2
ZBLOCK = 3
SBLOCK = 4
JBLOCK = 5
LBLOCK = 6


##############################
# Game methods
##############################

def game_over():
    global state

    menu_x = WIDTH / 2 - 100
    menu_y = HEIGHT / 2 - 40
    pygame.draw.rect(screen, WHITE, (menu_x, menu_y, 200, 80)) 
    pygame.draw.rect(screen, BLACK, (menu_x + 1, menu_y + 1, 198, 78))
    pygame.draw.rect(screen, WHITE, (menu_x + 2, menu_y + 2, 196, 76))

    text, textrect = create_text('Game Over!', BLACK, WHITE)
    screen.blit(text, (WIDTH / 2 - (textrect.width / 2), HEIGHT / 2 - 30))

    selection = LEFT
    while state == GAME_OVER:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                   selection = LEFT
                if event.key == pygame.K_d:
                    selection = RIGHT

                if event.key == pygame.K_RETURN:
                    if selection == LEFT:
                        state = RUN
                        reset()

                    if selection == RIGHT:
                        pygame.quit()
                        quit()
        
        if selection == LEFT:
            text, textrect = create_text('Again?', WHITE, BLACK)
            screen.blit(text, (menu_x + 30, HEIGHT / 2))
            text, textrect = create_text('Quit', BLACK, WHITE)
            screen.blit(text, (menu_x + (170 - textrect.right), HEIGHT / 2))
                
        if selection == RIGHT:
            text, textrect = create_text('Again?', BLACK, WHITE)
            screen.blit(text, (menu_x + 30, HEIGHT / 2))
            text, textrect = create_text('Quit', WHITE, BLACK)
            screen.blit(text, (menu_x + (170 - textrect.right), HEIGHT / 2))
                
        block.update()
        clock.tick(FPS)  

def create_text(text, color, background):
    textsurface = font.render(text, True, color, background)
    return textsurface, textsurface.get_rect()

def rand_block():
    return Block(random.randint(0,6))

def can_move_left(cur_block, deadsquares):
    for square in cur_block.squares:
        for dead in deadsquares.deadsquare_list:
            if square.rect.x - 20 == dead.rect.x and square.rect.y == dead.rect.y:
                return False

    return True

def can_move_right(cur_block, deadsquares):
    for square in cur_block.squares:
        for dead in deadsquares.deadsquare_list:
            if square.rect.x + 20 == dead.rect.x and square.rect.y == dead.rect.y:
                return False

    return True

def can_rotate_right(cur_block, deadsquares):
    temp_block = Block(cur_block.block_type)

    temp_block.rotate_right()
    if temp_block.check_collide:
        return False
    else:
        return True

def can_rotate_left(cur_block, deadsquares):
    temp_block = Block(cur_block.block_type)

    temp_block.rotate_left()
    if temp_block.check_collide:
        return False
    else:
        return True


##############################
# Main game code 
##############################

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
pygame.font.init()
font = pygame.font.SysFont(None, 20)
clock = pygame.time.Clock()

screen.fill(BLACK)

# Create Sprites
all_sprites = pygame.sprite.Group()     # list of all currently displayed sprites

cur_block = rand_block()
cur_block.set_next()
cur_block.set_current()
cur_block.display(all_sprites)

next_block = rand_block()
next_block.set_next()
next_block.display(all_sprites)

deadsquares = Deadsquares()



speed_timer = 0
speed = NORMSPEED

running = True
while running:

    # Process input (events)
    events = pygame.event.get()
    for event in events:
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
    

    # Check key pressed. Will trigger speed_time / 3 times per loop if key held
    keys = pygame.key.get_pressed()
    if speed_timer % 3 == 0:
        if keys[pygame.K_a] and can_move_left(cur_block, deadsquares):
           cur_block.move_left()
        if keys[pygame.K_d] and can_move_right(cur_block, deadsquares):
            cur_block.move_right()
        if keys[pygame.K_s] and not cur_block.check_collide(deadsquares):
            cur_block.move_down()
   
    # Check key pressed down. Only executes once when key pressed down
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e and can_rotate_right(cur_block, deadsquares):
                cur_block.rotate_right()
            if event.key == pygame.K_q and can_rotate_left(cur_block, deadsquares):
                cur_block.rotate_left()

            if event.key == pygame.K_SPACE:
                cur_block.fast_move(deadsquares)
                deadsquares.add_block(cur_block)
                cur_block = next_block
                cur_block.set_current()
                # next_block = rand_block()
                next_block = Block(LINE)

                next_block.set_next()
                next_block.display(all_sprites)


    # Updates falling block
    if speed_timer % speed == 0:
        collide = cur_block.check_collide(deadsquares)
      
        if collide:
            deadsquares.add_block(cur_block)
            cur_block = next_block
            cur_block.set_current()
            # next_block = rand_block()
            next_block = Block(LINE)

            next_block.set_next()
            next_block.display(all_sprites)

            collide = False
        else:
            cur_block.move_down()
        

    # Keep loop running at the right speed
    clock.tick(FPS)
    speed_timer += 1

    
    # Draw / render
    screen.fill(BLACK)

    # Draws white outer box
    pygame.draw.rect(screen, WHITE, (BOARDLEFT - 2, BOARDTOP - 2, BOARDWIDTH + 4, BOARDHEIGHT + 4), 1)
    # Draws hold box
    pygame.draw.rect(screen, WHITE, (BOARDRIGHT + 18, BOARDTOP - 2, 74, 94), 1)
    all_sprites.draw(screen) 
    text, textrect = create_text('NEXT', WHITE, BLACK)
    screen.blit(text, (BOARDRIGHT + 35, BOARDTOP - 20))

    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

