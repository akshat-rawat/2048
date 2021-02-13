# used MCST algorithm

from logic import random_move, move_down, move_left, move_right, move_up, add_new_2, get_current_state
from copy import deepcopy

def ai_move(board, searches_per_move, search_length):
    moves = [move_left, move_up, move_down, move_right]                 # list of all moves
    score_list = [0 for _ in range(4)]

    for i in range(4):
        current_matrix = deepcopy(board)
        initial_move = moves[i]                                         # make first move

        current_matrix, move_made, first_move_score = initial_move(current_matrix)
        if move_made:
            current_matrix = add_new_2(current_matrix)
            score_list[i] += first_move_score
        else:
            continue

        for _ in range(searches_per_move):                              # search different moves
            move_number = 1
            search_board = deepcopy(current_matrix)
            game_valid = True
            while game_valid and move_number < search_length:           # search on the selected move to certain depth
                search_board, game_valid, score = random_move(search_board)
                if game_valid:
                    search_board = add_new_2(search_board)
                    score_list[i] += score                              # add the score after making move
                    move_number += 1

    best_move_index = score_list.index(max(score_list))

    best_move = moves[best_move_index]                              # select best possible move i.e move with max score
    search_board, game_valid, score = best_move(board)

    return search_board, game_valid
