'''
As the input data you will get the multiline string consists of '0' & '#'.
where '0' means the empty piece of the ground and the '#' is the piece of your house.
Your task is to count
the minimal area of the rectangle ground which is enough for the building.
'''


def house(plan):
    new_plan = plan.split()
    number_rows = len(new_plan)
    number_columns = len(new_plan[0])

    a, b = 0, 0
    for i, lst in enumerate(new_plan, 1):
        if '#' in lst:
            a = i
            break
        else:
            a = 0

    for i, lst in enumerate(reversed(new_plan), 1):
        if '#' in lst:
            b = i
            break
        else:
            b = 0
    lenght = 0

    if a == 0 and b == 0:
        lenght = 0
    else:
        lenght = number_rows - a - b + 2

    g = []
    for line in new_plan:
        if '#' in line:
            g.append(list(line))

    no_zero_ending = []
    for lst in g:
        for i, x in enumerate(lst, 1):
            if x == '#':
                no_zero_ending.append(i)

    try:
        m = max(no_zero_ending)
    except ValueError:
        m = 0

    try:
        mi = min(no_zero_ending)
    except ValueError:
        mi = 0

    width = m - mi + 1

    return lenght * width


if __name__ == '__main__':
    print("Example:")
    print(house("\n0000000000\n000###0000\n000#######\n000###0000\n"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
