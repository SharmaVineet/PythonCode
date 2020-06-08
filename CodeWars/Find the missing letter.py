import string


def find_missing_letter(chars):
    subset_of_array = list(string.ascii_letters)[
                      list(string.ascii_letters).index(chars[0]):list(string.ascii_letters).index(chars[0]) + len(
                          chars) + 1]
    return "".join([i for i in subset_of_array if i not in chars])


if __name__ == '__main__':
    print(find_missing_letter(["a", "b", "c", "d", "f"]))
