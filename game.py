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

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# player sprite class - extends pygame's sprite class
# surface on the screen is an attribute of the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

# initializes game
pygame.init()

# creates screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# instantiates a player
player = Player()

# starts the game loop
running = True

while running:
    # looks at each event in the queue
    for event in pygame.event.get():
        # checks if user hit a key - not checking for only the down key
        if event.type == KEYDOWN:
            # stops loop if escape key hit
            if event.key == K_ESCAPE:
                running = False
        
        # stops loop and closes window if the user clicks the close button
        elif event.type == QUIT:
            running = False

    # gives surface a color to separate it from background
    screen.fill((0, 0, 0))

    # blit copies the contents of one surface to another
    screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    pygame.display.flip()
