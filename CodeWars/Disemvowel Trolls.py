def disemvowel(string):
    string = list(string)
    for num in string[:]:
        if num.lower() in ['a', 'i', 'o', 'u', 'e']:
            for _ in range(string.count(num)):
                string.remove(num)
    return "".join(string)


if __name__ == '__main__':
    print(disemvowel("What are you a communist"))
