import pygame
import os

# objects

# setup
worldx = 800
worldy = 600

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'stage.png').convert())
backdropbox = world.get_rect()

BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)

fps = 40 #frame rate
ani = 4 #animation cycles
clock = pygame.time.Clock()
pygame.init()

# main game loop