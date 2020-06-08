def perimeter(n):
    count = 1
    fibonacci_numbers = [1, 1]
    first, second = fibonacci_numbers
    while count != n:
        next_number = first + second
        first = second
        second = next_number
        count += 1
        fibonacci_numbers.append(next_number)
    return 4 * sum(fibonacci_numbers)


if __name__ == '__main__':
    print(perimeter(10))
