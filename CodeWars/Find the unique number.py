def find_uniq(arr):
    for n in list(set(arr)):
        if arr.count(n) == 1:
            return n


if __name__ == '__main__':
    a = [1, 1, 1, 2, 1, 1]
    b = [0, 0, 0.55, 0, 0]
    print(find_uniq(b))
