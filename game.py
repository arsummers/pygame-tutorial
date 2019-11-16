import pygame
import os
import sys

class Player(pygame.sprite.Sprite):
    """
    spawns a player
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images','hero' + str(i) + '.png'))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

# objects

# setup
worldx = 800
worldy = 600

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images','stage.png'))
backdropbox = world.get_rect()

BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)

fps = 40 #frame rate
ani = 4 #animation cycles
clock = pygame.time.Clock()
pygame.init()

# main game loop

running = True

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        
        # checks if a key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                running = False
        
    # fills world with background image
    world.blit(backdrop, backdropbox)

    pygame.display.flip()
    clock.tick(fps)