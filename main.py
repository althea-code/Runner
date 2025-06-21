import pygame
from sys import exit

pygame.init()

# create display surface
screen = pygame.display.set_mode((800,400))

# set window menu bar tile
pygame.display.set_caption('Runner')

# create clock object
clock = pygame.time.Clock()

# create a surface objects
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
player_surface = pygame.image.load('graphics/player.png')


while True:

    for event in pygame.event.get():

        # check to see if player has pressed the exit button in window
        if event.type == pygame.QUIT:
            # end initialized pygame process
            pygame.quit()
            # close any remaining code
            exit()

    # draw sky onto display screen
    screen.blit(sky_surface, (0,0))

    # draw ground onto display screen
    screen.blit(ground_surface, (0,300))

    # draw player onto display screen
    screen.blit(player_surface, (50,220))

    # updates screen's display surface
    pygame.display.update()

    # limit framerate
    clock.tick(60)