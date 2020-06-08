import string


def pig_it(text):
    first = text.split()
    for i, num in enumerate(first):
        if num not in string.punctuation:
            first[i] = "".join(list(num)[1:]) + list(num).pop(0) + 'ay'
        else:
            first[i] = num
    return " ".join(first)


if __name__ == '__main__':
    a = 'Pig latin is cool'
    print(pig_it(a))
