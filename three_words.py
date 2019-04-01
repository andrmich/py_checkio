def checkio(words: str) -> bool:
    list = words.split(' ')
    count = 0
    for e in list:
        if e.isalpha():
            count += 1
            if count >= 3:
                return True
        else:
            count = 0
    if count < 3:
        return False

    # words = words.split()
    #
    # for i in range(len(words) - 2):
    #
    #     if (words[i].isalpha() and words[i + 1].isalpha() and words[i + 2].isalpha()):
    #         return True
    #
    # return False

    # L=words.split()
    # if (len(L)<3):
    #   return False
    # i=1
    # while (i+1)<len(L):
    #   if (L[i-1].isalpha() and L[i].isalpha() and L[i+1].isalpha()):
    #       return True
    #       break
    #    i=i+1
    # return False

#bool(re.search(r'\D[A-z]+ [A-z]+ [A-z]+\D', words)) [True if found]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
