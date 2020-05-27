import os
import random

all_choices = ['Rock', 'Paper', 'Scissor']
all_players = ['computer', 'player']


def computer_move():
    computer_pick = random.choice(all_choices)
    return computer_pick


def player_move():
    player_pick = input("Please Pick from : \nR for Rock, \nP for Paper, \nS for Scissor\n")
    if player_pick:
        if player_pick == 'S':
            pick = 'Scissor'
        elif player_pick == 'R':
            pick = 'Rock'
        elif player_pick == 'P':
            pick = 'Paper'
        else:
            _ = os.system('clear')
            pick = player_move()
    else:
        _ = os.system('clear')
        pick = player_move()
    return pick


def rock_paper(computer_picked, player_picked):
    if computer_picked == 'Rock' and player_picked == 'Paper':
        return 'Player'
    elif computer_picked == 'Paper' and player_picked == 'Rock':
        return 'Computer'
    else:
        return 'Tied'


def paper_scissor(computer_picked, player_picked):
    if computer_picked == 'Paper' and player_picked == 'Scissor':
        return 'Player'
    elif computer_picked == 'Scissor' and player_picked == 'Paper':
        return 'Computer'
    else:
        return 'Tied'


def scissor_rock(computer_picked, player_picked):
    if computer_picked == 'Scissor' and player_picked == 'Rock':
        return 'Player'
    elif computer_picked == 'Rock' and player_picked == 'Scissor':
        return 'Computer'
    else:
        return 'Tied'


def declare_winner(computer_picked, player_picked):
    if computer_picked in ['Rock', 'Paper'] and player_picked in ['Rock', 'Paper']:
        return rock_paper(computer_picked, player_picked)
    elif computer_picked in ['Scissor', 'Paper'] and player_picked in ['Scissor', 'Paper']:
        return paper_scissor(computer_picked, player_picked)
    elif computer_picked in ['Scissor', 'Rock'] and player_picked in ['Scissor', 'Rock']:
        return scissor_rock(computer_picked, player_picked)


if __name__ == '__main__':
    is_game_on = True
    while is_game_on:
        print("Ready to Play Rock Paper Scissor!!")
        who_shall_play_first = random.choice(all_players)
        if who_shall_play_first == 'computer':
            pick_of_computer = computer_move()
            pick_of_player = player_move()
        else:
            pick_of_player = player_move()
            pick_of_computer = computer_move()
        winner = declare_winner(pick_of_computer, pick_of_player)
        print("YOU chose {} and COMPUTER chose {}\n".format(pick_of_player, pick_of_computer))
        if winner == 'Tied':
            print("Game has been tied!!\n")
        elif winner == 'Computer':
            print("COMPUTER won this game!!\n")
        else:
            print("YOU won this game!!\n ")
        play_again = input("Press y to play again: ")
        if play_again not in ['y', 'Y']:
            is_game_on = False
