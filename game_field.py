import consts
import screen
import random

place_grass_list = []
mine_field=[[consts.CELL_EMPTY for i in range(consts.BOARD_COLS)] for j in range(consts.BOARD_ROWS)]
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

    for row in range(consts.flag_row,consts.flag_row+consts.FLAG_ROWS):
        for col in range(consts.flag_col, consts.flag_col + consts.FLAG_COLS):
            mine_field[row][col]=consts.CELL_FLAG

    gen_mines()



    return


def gen_mines():
    for i in range(20):
        x = random.randint(0, consts.BOARD_COLS - 4)
        y = random.randint(0, consts.BOARD_ROWS - 4)
        while not check_can_place_mines((x,y)):
            x = random.randint(0, consts.BOARD_COLS - 4)
            y = random.randint(0, consts.BOARD_ROWS - 4)

        for col in range(x,x+3):
            mine_field[y][col]=consts.CELL_MINE

        x=x*consts.CELL_SIZE+20
        y=y*consts.CELL_SIZE-20
        mines_positions.append((x, y))
    return



def check_can_place_mines(mine_pos):
    x,y=mine_pos
    if x<consts.SOLDIER_COLS and y<consts.SOLDIER_ROWS:
        return False
    if mine_field[y][x]!=consts.CELL_EMPTY or mine_field[y][x+1]!=consts.CELL_EMPTY or mine_field[y][x+2]!=consts.CELL_EMPTY :
        return  False

    return True















