def anagrams(word, words):
    return [i for i in words if "".join(sorted(word)) == "".join(sorted(i))]


if __name__ == '__main__':
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
