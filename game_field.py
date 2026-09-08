import consts
import random


mine_field=[]
mines_positions=[]
grass_positions=[]

def gen_minefield():
    mine_field=[[consts.CELL_EMPTY for i in range(consts.BOARD_COLS)] for j in range(consts.BOARD_ROWS)]
    mine_field[consts.flag_row][consts.flag_col]=consts.CELL_FLAG
    return

def gen_mines():
    pass






