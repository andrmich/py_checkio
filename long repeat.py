def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    from itertools import groupby
    if line == '':
        return 0
    list = [''.join(g) for _, g in groupby(line)]
    longest = sorted(list, key = len, reverse=True)
    answer = len(longest[0])
    return answer

#
# count = 0
#
#     for i in set(line):
#
#         max_line = re.findall('['+str(i)+']+',line)
#
#         for j in max_line:
#
#             if len(j) > count:
#
#                 count = len(j)
#
#     return count
#


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
