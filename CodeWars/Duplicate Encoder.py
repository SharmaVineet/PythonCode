def duplicate_encode(word):
    return "".join([")" if word.lower().count(i) > 1 else "(" for i in word.lower()])


if __name__ == '__main__':
    print(duplicate_encode("QTGcJ(kwwc(IITOGHabxcQm!eTeF@dlbb"))
