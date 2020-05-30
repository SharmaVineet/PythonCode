import random

import hangman_words

word = list(hangman_words.words())
word_to_be_shown_at_end = "".join(word)
random.shuffle(word)


def anagram():
    number_of_guesses = 3
    run_again = True
    while run_again:
        capture_guess = input("Guess the Word \"{}\" : ".format("".join(word))).lower()
        number_of_guesses -= 1
        if capture_guess == word_to_be_shown_at_end:
            print("Congratulations you have guessed the correct word : {}".format(word_to_be_shown_at_end))
            run_again = False
        elif number_of_guesses == 0:
            print("You are out of guesses!! Word was : {}".format(word_to_be_shown_at_end))
            run_again = False
        else:
            print("Wrong Guess!! You have {} more guesses".format(number_of_guesses))


if __name__ == '__main__':
    print("This is an ANAGRAM Game!! You have 3 chances to the guess the word")
    anagram()
