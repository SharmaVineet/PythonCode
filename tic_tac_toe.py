import random
import sys

a = [' '] * 10
all_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def display_intro(name):
    print("Hi {} !! Welcome to the Tic Tac Toe Game".format(name))


def pick_choice(name):
    player_choice = input("\nPlease pick 0 or X to start the game: ").upper()
    if player_choice == '0':
        computer_choice = 'X'
        choices = {'player_choice': player_choice, 'computer_choice': computer_choice}
    elif player_choice == 'X':
        computer_choice = '0'
        choices = {'player_choice': player_choice, 'computer_choice': computer_choice}
    else:
        choices = pick_choice(name)
    return choices


def get_board(choice, selection=0):
    a[selection] = choice
    print("\n TIC TAC TOE BOARD ")
    print('[--------------]')
    print('[    |    |    ]')
    print('[ ' + a[1] + '  | ' + a[2] + '  | ' + a[3] + '  ]')
    print('[    |    |    ]')
    print('[--------------]')
    print('[    |    |    ]')
    print('[ ' + a[4] + '  | ' + a[5] + '  | ' + a[6] + '  ]')
    print('[    |    |    ]')
    print('[--------------]')
    print('[    |    |    ]')
    print('[ ' + a[7] + '  | ' + a[8] + '  | ' + a[9] + '  ]')
    print('[    |    |    ]')
    print('[--------------]')


def is_winner():
    if a[1] == a[2] == a[3] == 'X' or a[4] == a[5] == a[6] == 'X' or a[7] == a[8] == a[9] == 'X' or a[1] == a[4] == a[
        7] == 'X' or a[2] == a[5] == a[8] == 'X' or a[3] == a[6] == a[9] == 'X' or a[1] == a[5] == a[9] == 'X' or a[
        3] == a[5] == a[7] == 'X' or a[1] == a[2] == a[3] == '0' or a[4] == a[5] == a[6] == '0' or a[7] == a[8] == a[
        9] == '0' or a[1] == a[4] == a[7] == '0' or a[2] == a[5] == a[8] == '0' or a[3] == a[6] == a[9] == '0' or a[
        1] == a[5] == a[9] == '0' or a[3] == a[5] == a[7] == '0':
        return True
    return False


def player_move(choices):
    if not is_winner():
        move = int(input(player_name + "'s Turn!! Please Select the place from 1-9 "))
        if move in all_moves and move:
            get_board(choices['player_choice'], move)
            all_moves.remove(move)
            computer_move(choices)
        else:
            print("Place {} is already taken!!".format(move))
            player_move(choices)
    else:
        print("Computer has won the Game!!")
        sys.exit(0)


def computer_move(choices):
    if not is_winner():
        print("Computer Turn!! ")
        move = random.choice(all_moves)
        if move in all_moves and move:
            get_board(choices['computer_choice'], move)
            all_moves.remove(move)
            player_move(choices)
        else:
            print("Place {} is already taken!!".format(move))
            computer_move(choices)
    else:
        print("{} has won the Game!!".format(player_name))
        sys.exit(0)


if __name__ == '__main__':
    player_name = input("Please enter your game: ")
    display_intro(name=player_name)
    player_choices = pick_choice(name=player_name)
    print("{} chose {} and Computer chose {}\n".format(player_name, player_choices['player_choice'],
                                                       player_choices['computer_choice']))
    who_plays_first = random.choice(list(player_choices.keys()))
    if who_plays_first == 'player_choice':
        player_move(player_choices)
    else:
        computer_move(player_choices)
