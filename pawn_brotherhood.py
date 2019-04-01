def safe_pawns(pawns: set) -> int:
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    possible_moves = []
    for e in pawns:
        letter = e[::][0]
        number = int(e[::][1])
        if letter == 'a':
            m2_letter = str(columns[columns.index(letter) + 1])
            m2_number = str(number + 1)
            m2 = m2_letter + m2_number
            possible_moves.append(m2)
        elif letter == 'h':
            m1_letter = str(columns[columns.index(letter) - 1])
            m1_number = str(number + 1)
            m1 = m1_letter + m1_number
            possible_moves.append(m1)
        elif number == 8:
            possible_moves.append('')
        else:
            try:
                m1_letter = str(columns[columns.index(letter) - 1])
                m1_number = str(number + 1)
                m1 = m1_letter + m1_number
                possible_moves.append(m1)
            except IndexError:
                possible_moves.append('')
            try:
                m2_letter = str(columns[columns.index(letter) + 1])
                m2_number = str(number + 1)
                m2 = m2_letter + m2_number
                possible_moves.append(m2)
            except IndexError:
                possible_moves.append('')

    unique_possible_moves = set(possible_moves)
    answer = 0
    for e in pawns:
        if e in unique_possible_moves:
            answer += 1
    print (answer)

#safe_pawns(["a1","a2","a3","a4","h1","h2","h3","h4"])


# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
#     assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
