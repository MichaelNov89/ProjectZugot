import game_field
import consts

player_head_pos = (0, 0)
player_l_leg_pos = (player_head_pos[0],
                    player_head_pos[1] + consts.SOLDIER_ROWS)
player_r_leg_pos = (player_head_pos[0] + 1,
                    player_head_pos[1] + consts.SOLDIER_ROWS)


def move_player(move_dir):
    if check_possible(move_dir):
        match move_dir:
            case "up":
                player_head_pos[0] -= 0
            case "down":
                player_head_pos[0] += 0
            case "left":
                player_head_pos[1] -= 0
            case "right":
                player_head_pos[1] += 0


def check_possible(move_dir):
    match move_dir:
        case "up":
            if player_head_pos[0] - 1 < 0:
                return False

        case "down":
            if player_l_leg_pos[0] + 1 >= consts.SOLDIER_ROWS:
                return False

        case "left":
            if player_l_leg_pos[1] - 1 < 0:
                return False

        case "right":
            if player_r_leg_pos[1] + 1 >= consts.BOARD_COLS:
                return False
    return True


def check_on_bomb():
    l_leg_x = player_l_leg_pos[1]
    l_leg_y = player_l_leg_pos[0]
    r_leg_x = player_r_leg_pos[1]
    r_leg_y = player_r_leg_pos[0]
    if (game_field.mine_field[l_leg_y][l_leg_x] == consts.CELL_MINE )or (game_field.mine_field[r_leg_y][r_leg_x] == consts.CELL_MINE):
        return True
    return False

def check_on_mines():
    l_leg_x = player_l_leg_pos[1]
    l_leg_y = player_l_leg_pos[0]
    r_leg_x = player_r_leg_pos[1]
    r_leg_y = player_r_leg_pos[0]
    if (game_field.mine_field[l_leg_y][l_leg_x] == consts.CELL_FLAG )or (game_field.mine_field[r_leg_y][r_leg_x] == consts.CELL_FLAG):
        return True
    return False


