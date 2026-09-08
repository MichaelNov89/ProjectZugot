import pygame
from sys import exit
import consts

pygame.init()
window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
def screen_display():
    pygame.display.set_caption("The Flag")#title
    window.fill((63, 120, 11))
    pygame.display.update()
    background = pygame.image.load("background.png")




