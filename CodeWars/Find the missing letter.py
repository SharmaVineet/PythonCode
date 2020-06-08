import string


def find_missing_letter(chars):
    if chars[0].isupper():
        all_letters = list(string.ascii_uppercase)
    else:
        all_letters = list(string.ascii_lowercase)
    length_of_array = len(chars)
    index_of_first_letter = all_letters.index(chars[0])
    subset_of_array = all_letters[index_of_first_letter:index_of_first_letter + length_of_array + 1]
    return "".join([i for i in subset_of_array if i not in chars])


if __name__ == '__main__':
    print(find_missing_letter(['O', 'Q', 'R', 'S']))
