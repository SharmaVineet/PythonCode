def sum_of_intervals(intervals):
    set_of_item = set()
    for interval in intervals:
        right, left = interval
        while right != left:
            set_of_item.add((right, right + 1))
            right += 1
    return len(set_of_item)


if __name__ == '__main__':
    print(sum_of_intervals([(1, 5), (6, 10), (3, 4)]))
