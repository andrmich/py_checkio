def checkio(str_number: str, radix: int) -> int:
    numbers = list(range(0, 37))
    import string
    letters = list(string.ascii_uppercase)
    numbers_2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    let_num = numbers_2 + letters
    dic = dict(zip(let_num, numbers))
    answer = 0
    rev = str_number[::-1]
    n = 0
    for l in rev:
        if dic[l] >= radix:
            return -1
        else:
            answer += ((radix ** n) * dic[l])
            n += 1
    print( answer

# lambda s,r: int(s,r) if int(max(s),36) < r else -1

checkio('909',9)

            # These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
