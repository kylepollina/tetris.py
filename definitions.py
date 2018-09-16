# definitions.py
#  Definitions of constants for tetris game
#  Author: Kyle Pollina

# Built in constants
TITLE       = "Tetris"
GAME_OVER   = 0
RUN         = 1
PAUSE       = 2
WIDTH       = 20*20
HEIGHT      = 20*30
FPS         = 30

# User made constants
BOARDWIDTH  = 20*10
BOARDHEIGHT = 20*20
BOARDLEFT   = 5*20
BOARDRIGHT  = 15*20
BOARDTOP    = 5*20
BOARDBOT    = 25*20


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
