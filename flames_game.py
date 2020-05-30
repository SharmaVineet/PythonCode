def compare(boy, girl):
    for char in boy[:]:
        if char in girl:
            boy.remove(char)
            girl.remove(char)
    return len(boy + girl)


def get_flames_letter(length_of_name):
    return list('flames')[::-1][:(length_of_name % 6) + 1][-1]


def get_meaning(letter):
    flames_dict = {'f': 'Friends', 'l': 'Love', 'a': 'Affection', 'e': 'Enemy', 'm': 'Marriage', 's': 'Siblings'}
    return flames_dict[letter]


def flames():
    boy_name = list(input("Please Enter the Boy\'s Name : ").lower())
    girl_name = list(input("Please Enter the Girl\'s Name : ").lower())
    length_of_name_together = compare(boy=boy_name, girl=girl_name)
    flames_letter = get_flames_letter(length_of_name=length_of_name_together)
    meaning_of_letter = get_meaning(letter=flames_letter)
    return meaning_of_letter


if __name__ == '__main__':
    print_flames = flames()
    print(print_flames)
