import sys
import time
import pygame
import consts
import screen

state_of_game={
    "game_state":consts.RUNNING_STATE,
    "window_opened":True

}
def main():
    game_state=consts.RUNNING_STATE
    pygame.init()

    while game_state==consts.RUNNING_STATE and state_of_game["window_closed"]==True:
        screen.screen_display(state_of_game)

    return


def end_game():
    time.sleep(3)
    pygame.quit()
    return

def check_events():

    return


#==============================================================================

if __name__ == "__main__":
    main()
import sys
import time
import pygame
import consts
import screen
import game_field

state_of_game={
    "p_pos":(0,0)

}

def main():
    game_state=consts.RUNNING_STATE
    pygame.init()
    game_field.random_place_grass()


    while game_state==consts.RUNNING_STATE:
        screen.screen_display(state_of_game)



    return


def end_game():
    time.sleep(3)
    pygame.quit()
    return



#==============================================================================

if __name__ == "__main__":
    main()