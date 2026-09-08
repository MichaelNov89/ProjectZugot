import sys
import time
import pygame
import consts

state_of_game={
    "p_pos":(0,0)


}
def main():
    game_state=consts.RUNNING_STATE
    pygame.init()

    while game_state==consts.RUNNING_STATE:
        screen.draw_game(state_of_game)

    return


def end_game():
    time.sleep(3)
    pygame.quit()
    return



#==============================================================================

if __name__ == "__main__":
    main()