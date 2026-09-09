import sys
import time
import pygame
import consts
import screen
import game_field
import soldier

state_of_game={
    "game_state":consts.RUNNING_STATE,
    "window_opened":True

}
def main():
    game_field.gen_minefield()
    game_field.random_place_grass()
    pygame.init()

    while state_of_game["game_state"]==consts.RUNNING_STATE and state_of_game["window_opened"]==True:
        user_events()

        if soldier.check_on_bomb():
            state_of_game["game_state"]=consts.LOSS_STATE
        elif soldier.check_on_flag():
            state_of_game["game_state"]=consts.WIN_STATE
        screen.screen_display(state_of_game)

    if state_of_game["game_state"]!=consts.RUNNING_STATE:
        end_game()

    return
def user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state_of_game["window_opened"] = False

        elif state_of_game["game_state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.K_UP:
            soldier.move_player("up")

        elif event.type == pygame.K_DOWN:
            soldier.move_player("down")

        elif event.type == pygame.K_LEFT:
            soldier.move_player("left")

        elif event.type == pygame.K_RIGHT:
            soldier.move_player("right")



def end_game():
    if state_of_game["game_state"]==consts.LOSS_STATE:
        screen.draw_lose_message()
    elif state_of_game["game_state"]==consts.WIN_STATE:
        screen.draw_win_message()
    time.sleep(3)
    pygame.quit()
    return

def check_events():

    return


#==============================================================================

if __name__ == "__main__":
    main()
mal = 0