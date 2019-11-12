import pygame

# imports controls
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# initializes game
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# starts the game loop
running = True

while running:
    # looks at each event in the queue
    for event in pygame.event.get():
        # checks if user hit a key - not checking for only the down key
        if event.type == KEYDOWN:
            # stops loop is escape key hit
            if event.key == K_ESCAPE:
                running = False
        
        # stops loop and closes window if the user clicks the close button
        elif event.type == QUIT:
            running = False

