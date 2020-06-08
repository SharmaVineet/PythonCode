def dirReduc(arr):
    for _ in range(len(arr) // 2):
        for i in range(len(arr) - 1):
            if (arr[i] == 'NORTH' and arr[i + 1] == 'SOUTH') or (arr[i] == 'SOUTH' and arr[i + 1] == 'NORTH') or (
                    arr[i] == 'EAST' and arr[i + 1] == 'WEST') or (arr[i] == 'WEST' and arr[i + 1] == 'EAST'):
                arr.pop(i)
                arr.pop(i)
                break
    return arr


if __name__ == '__main__':
    a = ["NORTH", "WEST", "SOUTH", "EAST"]
    b = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    print(dirReduc(a))
