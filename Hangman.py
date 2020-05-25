import os
import sys

import hangman_words

random_word = list(hangman_words.words())
word_guessing_list = ['_'] * len(random_word)
count = 10
already_used_words = []
guessed_wrong_flag = False


def bye():
    sys.exit(0)


def clear():
    _ = os.system('clear')


def display_intro():
    ask_user_name = input("Please Enter Your Name : ")
    print("Hi {} ! Welcome to the HangMan Game, You have 10 chances to guess the word\n".format(ask_user_name))
    ready = input("Type y if you are ready ")
    if ready == 'y':
        _ = os.system('clear')
        print("".join(word_guessing_list))
        guess_word()
    else:
        print("Bye")
        bye()


def guess_word():
    global count
    global already_used_words
    global guessed_wrong_flag
    guessed_word = input("Please guess the word: ")
    if guessed_word not in already_used_words and guessed_word:
        already_used_words.append(guessed_word)
        if guessed_word in random_word:
            for i, num in enumerate(random_word):
                if num == guessed_word:
                    word_index = i
                    word_guessing_list[word_index] = guessed_word
            if "".join(word_guessing_list) != "".join(random_word):
                clear()
                print("Used words {}".format(already_used_words))
                print("".join(word_guessing_list))
                if 10 > count >= 0 and guessed_wrong_flag:
                    print("You have {} chances".format(count))
                    hangman_words.get_shapes(count_chances=count)
            else:
                clear()
                print("".join(word_guessing_list))
                print("Congratulations!! You have completed the HangMan Game!!")
                bye()
        else:
            guessed_wrong_flag = True
            clear()
            print("Used words {}".format(already_used_words))
            print("".join(word_guessing_list))
            new_count = hangman_words.print_hangman(count_chances=count)
            count = new_count
        guess_word()
    else:
        print("Either Word {} is already used or Empty".format(guessed_word))
        guess_word()


if __name__ == '__main__':
    display_intro()
