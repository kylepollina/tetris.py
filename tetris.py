#"Tetris" Tetris game made with Pygame
# Author: Kyle Pollina
import pygame
import random
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

cur_block = Block(TBLOCK)
cur_block.display(all_sprites)

next_block = Block(LINE)
next_block.set_next()
next_block.display(all_sprites)

deadsquares = Deadsquares()



speed_timer = 0
speed = 20

running = True
while running:

    # Process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
    

    # Check key pressed
    if speed_timer % 3 == 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
           cur_block.move_left()
        if keys[pygame.K_d]:
            cur_block.move_right()




    # Updates falling block
    if speed_timer % speed == 0:
        collide = cur_block.check_collide()
      
        if collide:
            # TODO
            print("collide")
        else:
            cur_block.move_down()
        

    # Keep loop running at the right speed
    clock.tick(FPS)
    speed_timer += 1

    
    # Draw / render
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (BOARDLEFT - 2, BOARDTOP - 2, BOARDWIDTH + 4, BOARDHEIGHT + 4), 1)
    all_sprites.draw(screen)

    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

