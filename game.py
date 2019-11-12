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

# fills screen with white
screen.fill((255, 255, 255))

# creates a surface, passes in length and width
surf = pygame.Surface((50,50))

# gives surface a color to separate it from background
surf.fill((0, 0, 0))
rect = surf.get_rect()

# finds actual middle of the surface
surf_center = (
    (SCREEN_WIDTH-surf.get_width())/2,
    (SCREEN_HEIGHT-surf.get_height())/2
)

# blit copies the contents of one surface to another
screen.blit(surf, surf_center)
pygame.display.flip()
