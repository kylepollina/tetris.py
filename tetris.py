#"Tetris" Tetris game made with Pygame
# Author: Kyle Pollina
import pygame
import random
import block

# Define constants
WIDTH  = 360
HEIGHT = 360
FPS    = 12

GAME_OVER = 0
RUN = 1
PAUSE = 2


# Define colors
WHITE  = (255,255,255)
BLACK  = (0,0,0)
RED    = (255,0,0)
GREEN  = (0,255,0)
BLUE   = (0,0,255)

# Define block types
SQUARE = 0
LINE   = 1
TBLOCK = 2
ZBLOCK = 3
SBLOCK = 4
JBLOCK = 5
LBLOCK = 6


class block(pygame.sprite.Sprite):
    
    def __init__(self, block_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (HEIGHT / 2, WIDTH / 2)


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



# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
pygame.font.init()
font = pygame.font.SysFont(None, 20)

clock = pygame.time.Clock()
state = RUN


# Create Sprites
all_sprites = pygame.sprite.Group()
block = block(SQUARE)
all_sprites.add(block)

running = True
while running:

    if state == GAME_OVER:
        game_over()

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

