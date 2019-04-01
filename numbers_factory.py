def checkio(number):
    answer = []
    k = number
    while k > 9:
        for i in range(9, 1, -1):
            if k % i == 0:
                k = k // i
                if k <= 9:
                    answer += [k, i]
                    break

                else:
                    answer += [i]
                    break

        else:
            return 0

    answer = sorted(answer)
    result = ''
    for a in answer:
        r = str(a)
        result += r

    return int(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
