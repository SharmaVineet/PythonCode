import os
import random


def print_shape(start, second, third, fourth):
    print(start + '\n' + second + '\n' + third + '\n' + fourth + '\n' + start)


def dice_simulator():
    random_number = random.randint(1, 6)
    start = '[----------]'
    zero = '[          ]'
    one = '[    0     ]'
    two = '[  0   0   ]'
    three = '[  0 0 0   ]'

    shapes = {1: [zero, one, zero], 2: [zero, two, zero], 3: [one, one, one], 4: [two, zero, two], 5: [two, one, two],
              6: [three, three, three]}
    [second, third, fourth] = shapes[random_number]
    print_shape(start=start, second=second, third=third, fourth=fourth)


def run_again():
    ask_user = input("Press y to roll again: ")
    if ask_user == 'y':
        return True
    print("Exiting Dice Simulator")
    return False


if __name__ == '__main__':
    print("This is Dice Simulator")
    dice_simulator()
    while run_again():
        _ = os.system('clear')
        dice_simulator()
