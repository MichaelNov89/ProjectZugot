import consts

mine_field=[]
mines_positions=[]
grass_positions=[]

def gen_minefield():
    mine_field=[[consts.CELL_EMPTY for i in range(consts.BOARD_COLS)] for j in range(consts.BOARD_ROWS)]
    mine_field[0][0]=consts.CELL_PLAYER
    return mine_field


