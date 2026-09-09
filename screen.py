import pygame
import consts
import game_field
import soldier

pygame.init()
window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
grass_image =(pygame.image.load("res/grass.png"))
grass_image = pygame.transform.scale(grass_image, (consts.GRASS_SIZE * consts.CELL_SIZE, consts.GRASS_SIZE * consts.CELL_SIZE))

flag_image =(pygame.image.load("res/flag.png"))
flag_image = pygame.transform.scale(flag_image, (consts.FLAG_COLS * consts.CELL_SIZE, consts.FLAG_ROWS * consts.CELL_SIZE))


soldier_image =(pygame.image.load("res/soldier.png"))
soldier_image = pygame.transform.scale(soldier_image, (consts.FLAG_COLS * consts.CELL_SIZE, consts.FLAG_ROWS * consts.CELL_SIZE))

soldier_night_image =(pygame.image.load("res/soldier_night.png"))
soldier_night_image = pygame.transform.scale(soldier_night_image, (consts.FLAG_COLS * consts.CELL_SIZE, consts.FLAG_ROWS * consts.CELL_SIZE))

mine_image =(pygame.image.load("res/mine.png"))
mine_image = pygame.transform.scale(mine_image, (consts.FLAG_COLS * consts.CELL_SIZE, consts.CELL_SIZE))

font = pygame.font.SysFont(consts.FONT_NAME, consts.LOSE_FONT_SIZE)

pygame.init()


def screen_display(state_of_game):
    window.fill((63, 120, 11))
    create_grass()
    create_solider()
    screen_display_Xray()
    create_night_solider()
    create_mine()
    create_flag()
    draw_lose_message()
    draw_win_message()
    pygame.display.update()


def create_grass():
    for i in range(len(game_field.place_grass_list)):
        temp_place_grass = game_field.place_grass_list[i]
        window.blit(grass_image, temp_place_grass)

def create_flag():
    window.blit(flag_image, (consts.flag_col * 20, consts.flag_row * 20))

def create_solider():
    window.blit(soldier_image, (soldier.player_head_pos))

def create_night_solider():
    window.blit(soldier_night_image, (0, 0))


def screen_display_Xray():
    window.fill((0, 0, 0))
    blockSize = 20
    for x in range(0, consts.WINDOW_WIDTH, blockSize):
        for y in range(0, consts.WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(window, consts.GREEN, rect, 1)


def create_mine():
    for i in range(len(game_field.mines_positions)):
        temp_place_mine = game_field.mines_positions[i]
        window.blit(mine_image, temp_place_mine)


def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.LOCATION)

def draw_message(message, font_size, color, location):
    text_img = font.render(message, True, color)
    window.blit(text_img, location)
mal = 0


