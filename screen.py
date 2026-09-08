import pygame
from sys import exit
import consts

pygame.init()
window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

pygame.display.set_caption("The Flag")#title
while True:#game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill((63, 120, 11))
    pygame.display.update()
    background = pygame.image.load("background.png")



