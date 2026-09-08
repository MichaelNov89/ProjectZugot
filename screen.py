import pygame

import consts

import game_field

pygame.init()
window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
grass_image =(pygame.image.load("res/grass.png"))
grass_image = pygame.transform.scale(grass_image, (consts.GRASS_SIZE * consts.CELL_SIZE, consts.GRASS_SIZE * consts.CELL_SIZE))

flag_image =(pygame.image.load("res/flag.png"))
flag_image = pygame.transform.scale(flag_image, (consts.FLAG_COLS * consts.CELL_SIZE, consts.FLAG_ROWS * consts.CELL_SIZE))


soldier_image =(pygame.image.load("res/soldier.png"))
soldier_image = pygame.transform.scale(soldier_image, (consts.FLAG_COLS * consts.CELL_SIZE, consts.FLAG_ROWS * consts.CELL_SIZE))


pygame.init()


def screen_display(state_of_game):
    pygame.display.set_caption("The Flag")#title
    window.fill((63, 120, 11))
    create_grass()
    create_flag()
    create_solider()
    pygame.display.update()


def create_grass():
    for i in range(20):
        temp_place_grass = game_field.place_grass_list[i]
        window.blit(grass_image, temp_place_grass)

def create_flag():
    window.blit(flag_image, (consts.flag_col * 20, consts.flag_row * 20))

def create_solider():
    window.blit(soldier_image, (0, 0))


def screen_display_Xray():
    pygame.display.set_caption("Xray")






