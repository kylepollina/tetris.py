#"Tetris" Tetris game made with Pygame
# Author: Kyle Pollina
import pygame
import random

# Define constants
WIDTH  = 20*20
HEIGHT = 20*30
FPS    = 30

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


# Classes
class Square(pygame.sprite.Sprite):
    
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)


class Block:

    squares = []
    block_type = 0

    def __init__(self, block_type):
        self.block_type = block_type
   
        if self.block_type == SQUARE:
            self.square1 = Square(YELLOW)
            self.square2 = Square(YELLOW)
            self.square3 = Square(YELLOW)
            self.square4 = Square(YELLOW)

            self.square2.rect.left += 20
            self.square3.rect.top  += 20
            self.square4.rect.left += 20
            self.square4.rect.top  += 20

            self.squares.append(self.square1) 
            self.squares.append(self.square2) 
            self.squares.append(self.square3) 
            self.squares.append(self.square4) 

        if self.block_type == LINE:
            self.square1 = Square(CYAN)
            self.square2 = Square(CYAN)
            self.square3 = Square(CYAN)
            self.square4 = Square(CYAN)

            self.square2.rect.top  += 20
            self.square3.rect.top  += 40
            self.square4.rect.top  += 60

            self.squares.append(self.square1) 
            self.squares.append(self.square2) 
            self.squares.append(self.square3) 
            self.squares.append(self.square4) 

        if self.block_type == TBLOCK:
            self.square1 = Square(PURPLE)
            self.square2 = Square(PURPLE)
            self.square3 = Square(PURPLE)
            self.square4 = Square(PURPLE)

            self.square2.rect.top  += 20
            self.square3.rect.top  += 20
            self.square3.rect.left += 20
            self.square4.rect.top  += 40

            self.squares.append(self.square1) 
            self.squares.append(self.square2) 
            self.squares.append(self.square3) 
            self.squares.append(self.square4) 
            
        if self.block_type == ZBLOCK:
            self.square1 = Square(RED)
            self.square2 = Square(RED)
            self.square3 = Square(RED)
            self.square4 = Square(RED)

            self.square2.rect.left  += 20
            self.square3.rect.top   += 20
            self.square3.rect.left  += 20
            self.square4.rect.top   += 20
            self.square4.rect.left  += 40

            self.squares.append(self.square1) 
            self.squares.append(self.square2) 
            self.squares.append(self.square3) 
            self.squares.append(self.square4) 
            
        if self.block_type == SBLOCK:
            self.square1 = Square(GREEN)
            self.square2 = Square(GREEN)
            self.square3 = Square(GREEN)
            self.square4 = Square(GREEN)

            self.square1.rect.top   += 20
            self.square2.rect.left  += 20
            self.square3.rect.top   += 20
            self.square3.rect.left  += 20
            self.square4.rect.left  += 40

            self.squares.append(self.square1) 
            self.squares.append(self.square2) 
            self.squares.append(self.square3) 
            self.squares.append(self.square4) 

        if self.block_type == JBLOCK:
            self.square1 = Square(BLUE)
            self.square2 = Square(BLUE)
            self.square3 = Square(BLUE)
            self.square4 = Square(BLUE)

            self.square2.rect.top   += 20
            self.square3.rect.top   += 20
            self.square3.rect.left  += 20
            self.square4.rect.top   += 20
            self.square4.rect.left  += 40


            self.squares.append(self.square1) 
            self.squares.append(self.square2) 
            self.squares.append(self.square3) 
            self.squares.append(self.square4) 

        if self.block_type == LBLOCK:
            self.square1 = Square(ORANGE)
            self.square2 = Square(ORANGE)
            self.square3 = Square(ORANGE)
            self.square4 = Square(ORANGE)

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


# Game methods
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
                
        pygame.display.update()
        clock.tick(FPS)  

def create_text(text, color, background):
    textsurface = font.render(text, True, color, background)
    return textsurface, textsurface.get_rect()




# MAIN GAME CODE
# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
pygame.font.init()
font = pygame.font.SysFont(None, 20)
clock = pygame.time.Clock()


# Create Sprites
all_sprites = pygame.sprite.Group()
block = Block(LBLOCK)

running = True
while running:
    
    # Process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # keep loop running at the right speed
    clock.tick(FPS)
    
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

