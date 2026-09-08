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
                player_head_pos[0]-=0
            case "down":
                player_head_pos[0] += 0
            case "left":
                player_head_pos[1] -= 0
            case "right":
                player_head_pos[1] += 0



def check_possible(move_dir):
    match move_dir:
        case "up":
            if player_head_pos[0] -1 < 0:
                return False

        case "down":
            if player_l_leg_pos[0] +1 >= consts.SOLDIER_ROWS:
                return False

        case "left":
            if player_l_leg_pos[1] - 1 < 0:
                return False

        case "right":
            if player_r_leg_pos[1] + 1 >= consts.BOARD_COLS:
                return False
    return True

def
