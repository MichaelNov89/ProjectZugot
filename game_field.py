import consts
import screen
import random

place_grass_list = []
mine_field=[]
mines_positions=[]


def random_place_grass():
    for i in range(20):
        x = random.randint(0, consts.WINDOW_WIDTH-40)
        y = random.randint(0, consts.WINDOW_HEIGHT-40)
        while (x<=consts.CELL_SIZE*consts.SOLDIER_COLS and y<=consts.CELL_SIZE*consts.SOLDIER_ROWS ) or (x>=consts.CELL_SIZE*consts.flag_col-40 and y>=consts.CELL_SIZE*consts.flag_row-40):
            x = random.randint(0, consts.WINDOW_WIDTH - 40)
            y = random.randint(0, consts.WINDOW_HEIGHT - 40)
        place_grass_list.append((x,y))

def gen_minefield():
    mine_field=[[consts.CELL_EMPTY for i in range(consts.BOARD_COLS)] for j in range(consts.BOARD_ROWS)]
    mine_field[consts.flag_row][consts.flag_col]=consts.CELL_FLAG
    return

def gen_mines():
    pass

mal = 0














