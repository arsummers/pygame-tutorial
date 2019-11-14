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

    # method that moves the sprite based on user key press input
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        #  keeps player from running off the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

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

    # get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # updates sprite based on user key presses
    player.update(pressed_keys)

    # gives surface a color to separate it from background
    screen.fill((0, 0, 0))

    # blit copies the contents of one surface to another
    screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    pygame.display.flip()
