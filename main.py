import sys
import time
import pygame
import consts
import screen
import game_field
import soldier
import os
import database

clock = pygame.time.Clock()

state_of_game = {
    "game_state": consts.RUNNING_STATE,
    "window_opened": True

}


def main():
    game_field.gen_minefield()
    game_field.random_place_grass()
    pygame.init()

    while state_of_game["game_state"] == consts.RUNNING_STATE and \
            state_of_game["window_opened"] == True:

        user_events()
        if soldier.check_on_bomb():
            state_of_game["game_state"] = consts.LOSS_STATE
        elif soldier.check_on_flag():
            state_of_game["game_state"] = consts.WIN_STATE

        screen.screen_display(state_of_game)

    if state_of_game["game_state"] != consts.RUNNING_STATE:
        end_game()

    return


def user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state_of_game["window_opened"] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                soldier.move_player("up")

            if event.key == pygame.K_DOWN:
                soldier.move_player("down")

            if event.key == pygame.K_LEFT:
                soldier.move_player("left")

            if event.key == pygame.K_RIGHT:
                soldier.move_player("right")

            if event.key == pygame.K_RETURN:
                screen.screen_display_Xray()
                time.sleep(0.5)

            if event.key == pygame.K_1:
                first_time = time.time()
                state_of_game["press_start_time"] = first_time

            if event.key == pygame.K_2:
                first_time = time.time()
                state_of_game["press_start_time"] = first_time

            if event.key == pygame.K_3:
                first_time = time.time()
                state_of_game["press_start_time"] = first_time

            if event.key == pygame.K_4:
                first_time = time.time()
                state_of_game["press_start_time"] = first_time

            if event.key == pygame.K_5:
                first_time = time.time()
                state_of_game["press_start_time"] = first_time

            if event.key == pygame.K_6:
                first_time = time.time()
                state_of_game["press_start_time"] = first_time

            if event.key == pygame.K_7:
                first_time = time.time()
                state_of_game["press_start_time"] = first_time

            if event.key == pygame.K_8:
                first_time = time.time()
                state_of_game["press_start_time"] = first_time

            if event.key == pygame.K_9:
                first_time = time.time()
                state_of_game["press_start_time"] = first_time

        calc_time(event)

def calc_time(event):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
            current_time = time.time() - state_of_game["press_start_time"]
            number = event.unicode
            if current_time < 3:
                database.save_to_file(current_time, number)
            else:
                database.read_from_file(current_time, number)








def end_game():
    if state_of_game["game_state"] == consts.LOSS_STATE:
        screen.draw_lose_message()

    elif state_of_game["game_state"] == consts.WIN_STATE:
        screen.draw_win_message()

    time.sleep(3)
    pygame.quit()
    return


def check_events():
    return


# ==============================================================================

if __name__ == "__main__":
    main()
mal = 0
