import random
import string

password = []
all_values_for_password = [string.punctuation, string.ascii_lowercase, string.ascii_uppercase, string.digits]


def generate_password(length=12):
    for _ in range(length):
        random_value = random.choice(all_values_for_password)
        password.append(random.choice(random_value))

    return "Random Generated Password is \t{}".format("".join(password))


if __name__ == '__main__':
    number_of_character = input("Enter Password Length(Press \'Enter\' for default) : ")
    if not number_of_character:
        val = generate_password()
    else:
        val = generate_password(int(number_of_character))

    print(val)
