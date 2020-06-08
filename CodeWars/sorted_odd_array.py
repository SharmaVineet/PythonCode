def sort_array(source_array):
    odd_list = sorted([i for i in source_array if i % 2 != 0])
    for i, num in enumerate(source_array):
        if num % 2 != 0:
            source_array[i] = odd_list[0]
            odd_list.pop(0)
    return source_array


if __name__ == '__main__':
    print(sort_array([]))
