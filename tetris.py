#"My Game" Snake game made with Pygame
# Author: Kyle Pollina
import pygame
import random


# Define constants
WIDTH  = 360
HEIGHT = 360
FPS    = 12

UP     = 0
RIGHT  = 1
DOWN   = 2
LEFT   = 3

GAME_OVER = 0
RUN = 1
PAUSE = 2


# Define colors
WHITE  = (255,255,255)
BLACK  = (0,0,0)
RED    = (255,0,0)
GREEN  = (0,255,0)
BLUE   = (0,0,255)



# Sprite for the snake
class Snake(pygame.sprite.Sprite):

    body_array = []
    direction = RIGHT
    prev_head_x = 0
    prev_head_y = 0
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (HEIGHT / 2, WIDTH / 2)

        # Makes the snake 3 blocks long to start
        new_body1 = Body(self.rect.x - 20, self.rect.y) 
        new_body2 = Body(self.rect.x - 40, self.rect.y)
        self.body_array.append(new_body1)
        self.body_array.append(new_body2)
        all_sprites.add(new_body1, new_body2)

    def update(self):
        global state

        prev_head_x = self.rect.x
        prev_head_y = self.rect.y

        if self.direction == UP:
            self.rect.y -= 20
        if self.direction == LEFT:
            self.rect.x -= 20
        if self.direction == DOWN:
            self.rect.y += 20
        if self.direction == RIGHT:
            self.rect.x += 20

        for body in self.body_array:
            if (self.rect.x == body.rect.x) and (self.rect.y == body.rect.y):
                state = GAME_OVER

        if self.rect.x >= WIDTH or self.rect.y >= HEIGHT or self.rect.x < 0 or self.rect.y < 0:
            state = GAME_OVER


        # Update the body pieces
        body = self.body_array[-1]              # -1 gets last element of array. -2 would get 2nd to last etc.
        body.rect.x = prev_head_x
        body.rect.y = prev_head_y

        self.body_array.insert(0, body)         # adds the updated body to the front
        del self.body_array[-1]                 #removes the old body from the end

        
    def set_direction(self, d):
        if (d == UP and self.direction != DOWN or
            d == LEFT and self.direction != RIGHT or
            d == DOWN and self.direction != UP or
            d == RIGHT and self.direction != LEFT):
            self.direction = d

    def add_body(self, x, y):
        new_body = Body(x, y)
        self.body_array.append(new_body)
        all_sprites.add(new_body)
    
    def reset(self):
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (HEIGHT / 2, WIDTH / 2)

        self.body_array = []

        # Makes the snake 3 blocks long to start
        new_body1 = Body(self.rect.x - 20, self.rect.y) 
        new_body2 = Body(self.rect.x - 40, self.rect.y)
        self.body_array.append(new_body1)
        self.body_array.append(new_body2)
        all_sprites.add(new_body1, new_body2)

        self.direction = RIGHT
        prev_head_x = 0
        prev_head_y = 0

class Body(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    

class Apple(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH, 20)
        self.rect.y = random.randrange(0, HEIGHT, 20)

    # randomly generates a new location on the board
    def new_loc(self):
        global snake

        valid_loc = False
        while not valid_loc:
            x_new = random.randrange(0, WIDTH, 20)
            y_new = random.randrange(0, HEIGHT, 20)

            if (x_new != snake.rect.x) and (y_new != snake.rect.y):
                for body in snake.body_array:
                    if (x_new == body.rect.x) or (y_new == body.rect.y):
                        valid_loc = False
                        break
                    else:
                        valid_loc = True
                    
            self.rect.x = x_new 
            self.rect.y = y_new



def reset():
    global snake
    global apple
    global all_sprites

    all_sprites.empty()
    all_sprites.add(apple, snake)
    snake.reset()
    apple.new_loc()
    

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
pygame.display.set_caption("Snake")
pygame.font.init()
font = pygame.font.SysFont(None, 20)

clock = pygame.time.Clock()
state = RUN

# Create Sprites
all_sprites = pygame.sprite.Group()
apple = Apple()
snake = Snake()
all_sprites.add(apple, snake)



running = True
while running:


    if state == GAME_OVER:
        game_over()

    # Process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False

        # check key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake.set_direction(UP)
            if event.key == pygame.K_a:
                snake.set_direction(LEFT)
            if event.key == pygame.K_s:
                snake.set_direction(DOWN)
            if event.key == pygame.K_d:
                snake.set_direction(RIGHT)


    # Update
    all_sprites.update()

    if pygame.sprite.collide_rect(apple, snake):
        snake.add_body(apple.rect.x, apple.rect.y)
        apple.new_loc()
    
    # keep loop running at the right speed
    clock.tick(FPS)
    
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

