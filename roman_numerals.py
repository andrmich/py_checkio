first_ten = ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X')

second_ten = ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C')

third_ten = ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', 'M')

fourth_ten = ('', 'M', 'MM', 'MMM')


def checkio(data):
    answer = ''
    if data > 999:
        t, h = divmod(data, 1000)
        answer = fourth_ten[t]
        data = h

    if data > 99:
        nh, d = divmod(data, 100)
        answer += third_ten[nh]
        data = d

    if data > 9:
        nd, s = divmod(data, 10)
        answer += second_ten[nd]
        data = s

    if data > 0:
        answer += first_ten[data]

    return answer


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
