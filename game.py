import pygame
import os
import sys

# global colors to use
BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)
ALPHA = (1, 0, 128)

class Player(pygame.sprite.Sprite):
    """
    spawns a player
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 #move along x axis
        self.movey = 0 #move alone y axis
        self.frame = 0 #counts frames

        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images','hero' + str(i) + '.png'))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y
    
    def update(self):
        """
        update sprite position
        """
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        # move left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]
        # move right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[(self.frame//ani)+1]

class Enemy(pygame.sprite.Sprite):
    """
    spawns an enemy
    """
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Level():
    def bad(lvl, eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0], eloc[1], 'enemy.png')
            enemy_list = pygame.sprite.Group()
            enemy_list.add(enemy)
        if lvl == 2:
            print("Level " + str(lvl))
        return enemy_list
# objects

# setup

worldx = 800
worldy = 600

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images','stage.png'))
backdropbox = world.get_rect()

# brings a Player instance into the rest of the code
player = Player()
# starting positions
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10 #number of pixels to move

eloc = []
eloc = [200, 20]
enemy_list = Level.bad(1, eloc)


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
            running = False
        
        # checks if a key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                     player.control(steps, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(-steps, 0)
                   
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    running = False
        
    # fills world with background image
    world.blit(backdrop, backdropbox)
    player.update() #updates player position
    player_list.draw(world) #draws player
    enemy_list.draw(world) #draws enemy
    pygame.display.flip()
    clock.tick(fps)