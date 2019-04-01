def checkio(expression):
    result = []
    char_list = ['{', '}', '[', ']', '(', ')']
    open = [ord('{'), ord('['), ord('(')]
    end = [ord('}'), ord(']'), ord(')')]

    for char in expression:
        if char in char_list:
            result.append(ord(char))

    o_list = []

    for r in result:
        if r in open:
            o_list.append(r)
        else:
            if len(o_list)>0:
                if r - o_list[-1] == 1 or r - o_list[-1] == 2:
                    o_list.pop()
                else:
                    return False
            else:
                return False

    if len(o_list) == 0:
        return True
    else:
        return False



checkio("(((([[[{{{3}}}]]]]))))")

# # These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio("((5+3)*2+1)") == True, "Simple"
#     assert checkio("{[(3+1)+2]+}") == True, "Different types"
#     assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
#     assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
#     assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
#     assert checkio("2+3") == True, "No brackets, no problem"
