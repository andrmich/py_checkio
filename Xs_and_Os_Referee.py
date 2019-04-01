from typing import List

def checkio(game_result: List[str]) -> str:
    # horizontal
    for e in game_result:
        if e.count('X') == 3:
            return 'X'
        elif e.count('O') == 3:
            return 'O'
    #vertical
    else:
        n = 0
        for g in range(0,3):
            for f in range (0,3):
                if game_result[n][f] =='X' and game_result[n+1][f] == 'X' and game_result[n+2][f] =='X':
                    return 'X'
                elif game_result[n][f] == 'O' and game_result[n + 1][f] == 'O' and game_result[n + 2][f] == 'O':
                    return 'O'
            # diagonal
        else:
            if game_result[0][0] =='X' and game_result[1][1] == 'X' and game_result[2][2] =='X':
                return 'X'
            elif game_result[0][0] == 'O' and game_result[1][1] == 'O' and game_result[2][2] == 'O':
                return 'O'
            elif game_result[0][2] =='X' and game_result[1][1] == 'X' and game_result[2][0] =='X':
                return 'X'
            elif game_result[0][2] =='O' and game_result[1][1] == 'O' and game_result[2][0] =='O':
                return 'O'
            else:
                return 'D'

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")




# def checkio(result):
#
#     rows = result
#
#     cols = map(''.join, zip(*rows))
#
#     diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
#
#     lines = rows + list(cols) + list(diags)
#
#
#     return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'

