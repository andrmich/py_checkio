def checkio(number: int) -> int:
    count = 1
    for n in str(number):
        if int(n) != 0:
            count = count * int(n)

    return count

#lambda n: reduce(lambda x, y: x*y if not y == 0 else x, map(int, list(str(n))))

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
