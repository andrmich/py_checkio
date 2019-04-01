import pprint


def get_4_len_list(list):
    new_list = []
    for lst in list:
        if len(lst) >= 4:
            new_list += [lst]
    return new_list


def diagonal_NS_EW(size):
    r = []
    d_NS_EW = []
    N = size
    for n in range(0, N):
        for x in range(n + 1):
            y = n - x
            r.append([x, y])
        d_NS_EW.append(r)
        r = []

    s = []
    diag_2 = []
    for n in range(N, (2 * N)):
        for y in range(1, N):
            x = n - y
            if x < N:
                s.append([x, y])
        diag_2.append(s)
        s = []

    return d_NS_EW + diag_2


def diagonal_SN_WE(size):
    z = []
    diag_3 = []
    N = size

    for y in range(N - 1, 0, -1):
        x = 0
        z.append([x, y])
        while y < N - 1:
            x += 1
            y += 1
            z.append([x, y])
        diag_3.append(z)
        z = []

    t = []
    diag_4 = []

    for x in range(0, N):
        y = 0
        t.append([x, y])
        while x < N - 1:
            x += 1
            y += 1
            t.append([x, y])
        diag_4.append(t)
        t = []

    return diag_3 + diag_4


def back_to_values(diagonal, matrix):
    result = []
    e = []

    for element in diagonal:
        for ind in element:
            e.append(matrix[ind[0]][ind[1]])
        result.append(e)
        e = []
    return result


def checkio(matrix):
    rows = matrix

    col = list(zip(*rows))
    columns = [list(elem) for elem in col]

    d_NS_EW = diagonal_NS_EW(len(matrix))

    d_SN_WE = diagonal_SN_WE(len(matrix))

    diagonal = get_4_len_list(d_NS_EW) + get_4_len_list(d_SN_WE)

    result = back_to_values(diagonal, matrix)

    all = rows + columns + result
    pprint.pprint(all)
    answer = []

    for m in range(0, (len(all))):
        for n in range(1, len(all[m])):
            if all[m][n-1] == all[m][n]:
                answer.append(all[m][n])
                if len(answer) + 1 >= 4:
                    print(True)
            else:
                answer = []
    else:
        if answer == '':
            return False
        elif len(answer) + 1 < 4:
            return False




checkio([
    [2, 4, 1, 7],
    [1, 2, 4, 1],
    [9, 4, 2, 1],
    [5, 9, 2, 2]

])

# return True or False

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio([
#         [1, 2, 1, 1],
#         [1, 1, 4, 1],
#         [1, 3, 1, 6],
#         [1, 7, 2, 5]
#     ]) == True, "Vertical"
#     assert checkio([
#         [7, 1, 4, 1],
#         [1, 2, 5, 2],
#         [3, 4, 1, 3],
#         [1, 1, 8, 1]
#     ]) == False, "Nothing here"
#     assert checkio([
#         [2, 1, 1, 6, 1],
#         [1, 3, 2, 1, 1],
#         [4, 1, 1, 3, 1],
#         [5, 5, 5, 5, 5],
#         [1, 1, 3, 1, 1]
#     ]) == True, "Long Horizontal"
#     assert checkio([
#         [7, 1, 1, 8, 1, 1],
#         [1, 1, 7, 3, 1, 5],
#         [2, 3, 1, 2, 5, 1],
#         [1, 1, 1, 5, 1, 4],
#         [4, 6, 5, 1, 3, 1],
#         [1, 1, 9, 1, 2, 1]
#     ]) == True, "Diagonal"
