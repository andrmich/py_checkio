def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) == 0:
        return 0
    else:
        count = 0
        s = 0
        for e in array:
            if count % 2 == 0:
                s += e
            count += 1
    s = s * array[-1]
    return s
    # print(s)


# return sum(array[i]*array[-1] for i in range(0,len(array),2))

# if len(array) < 1:
#
#         return 0
#
#     sum = 0
#
#     for i in range(0, len(array), 2):
#
#         sum += array[i]
#
#     sum *= array[-1]
#
#     return sum


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
