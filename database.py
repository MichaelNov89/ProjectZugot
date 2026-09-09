import pandas as pd

import consts
import game_field
import soldier


def save_to_file(save_file_num):
    save_file_name="save"+str(save_file_num)+".csv"
    p_head_pos_filled= fill_list([soldier.player_head_pos.copy()])
    bomb_pos_list_filled=fill_list(game_field.mines_positions.copy())
    grass_pos_list_filled=fill_list(game_field.place_grass_list.copy())

    save_file={
        "p_head_pos": p_head_pos_filled,
        "bomb_pos_list": bomb_pos_list_filled,
        "grass_pos_list":grass_pos_list_filled,
        "game_field_matrix":game_field.mine_field
    }
    save_file=pd.DataFrame(save_file)
    save_file.to_csv(save_file_name)
    print(save_file)
    return

def fill_list(list_to_fill):
    while len(list_to_fill)<consts.BOARD_ROWS:
        list_to_fill.append("f")
    return list_to_fill


#NOT FINISHED NO READING SAVE
def read_from_file(save_file_num):
    save_file_name = "save" + str(save_file_num) + ".csv"
    save_data=pd.read_csv(save_file_name)
    head_pos=[]
    bomb_pos_list=[]
    grass_pos_list=[]
    game_field_matrix=[]

    return
