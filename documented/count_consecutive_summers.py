'''Compute how many different ways
 positive integer can be expressed as a sum of consecutive positive integers.
  For example, 42 can be expressed as such a sum in four different ways:
  (a) 3+4+5+6+7+8+9, (b) 9+10+11+12, (c) 13+14+15 and (d) 42.
 '''


def count_consecutive_summers(num):
    combination = []
    result = []
    for i in range(1, num + 1):
        combination.append(i)
        number = i
        while sum(combination) < num:
            number += 1
            combination.append(number)
        else:
            if sum(combination) == num:
                result.append(combination)
                combination = []
                continue
            else:
                combination = []
                continue
    return len(result)


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(99))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
