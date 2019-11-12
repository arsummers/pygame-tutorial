import pygame
pygame.init()

# drawing window
screen = pygame.display.set_mode([500, 500])

# runs until user tells it not to
running = True

while running:

    # checks if user clicked close window button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # makes the background white
    screen.fill((255, 255, 255))

    # draws a solid blue circle in center of screen
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    pygame.display.flip()

pygame.quit()