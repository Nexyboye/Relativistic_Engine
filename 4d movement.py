import pygame
import numpy

# POSITION
# 1 distance, 3 directions

# POSITION CHANGE:
# speed will be constant 1
# 1 temporal 3 spatial directions


# observer is the middle of the coord system
# observer always stationary, world moves around it, it is only the middle of the display
# observer is not defined at all in any way, this'll make the world infinite

# distance from observer



pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Relativistic Engine")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))
    pygame.display.flip()


pygame.quit()