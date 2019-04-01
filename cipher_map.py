def recall_password(cipher_grille, ciphered_password):
    first_grille = ''.join(cipher_grille)
    first_x = []
    for i, n in enumerate(first_grille):
        if n == 'X':
            first_x.append(i)
    password = ''.join(ciphered_password)
    first_let = ''.join([])
    for j in first_x:
        first_let += password[j]

    #+ 90
    second_grille = ''.join([])
    for m in range(0, 4):
       for k in range (3, -1, -1):
           second_grille += (cipher_grille[k][m])
    second_x = []
    for i, n in enumerate(second_grille):
        if n == 'X':
            second_x.append(i)
    second_let = ''.join([])
    for j in second_x:
        second_let += password[j]

    #+180
    third_grille = ''.join([])
    for m in range(3, -1, -1):
       for k in range (3, -1, -1):
           third_grille += (cipher_grille[m][k])
    third_x = []
    for i, n in enumerate(third_grille):
        if n == 'X':
            third_x.append(i)
    third_let = ''.join([])
    for j in third_x:
        third_let += password[j]

    #+270
    fourth_grille = ''.join([])
    for m in range(3, -1, -1):
       for k in range (0,4):
           fourth_grille += (cipher_grille[k][m])
    fourth_x = []
    for i, n in enumerate(fourth_grille):
        if n == 'X':
            fourth_x.append(i)
    fourth_let = ''.join([])
    for j in fourth_x:
        fourth_let += password[j]

    return first_let+ second_let+third_let+ fourth_let


SIZE = 4


def get_x_coords(grille):
    result = set()
    for i, row in enumerate(grille):
        for j, ch in enumerate(row):
            if ch == 'X':
                result.add((i, j))
    return result


def rotate_grille(x_coords):
    return {(j, SIZE - i - 1) for i, j in x_coords}


def recall_password(grille, page):
    x_coords = get_x_coords(grille)
    result = ""
    for _ in range(4):
        for i, row in enumerate(page):
            for j, letter in enumerate(row):
                if (i, j) in x_coords:
                    result += letter
        x_coords = rotate_grille(x_coords)
    return result





if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
