def repeat_inside(line):
    """
        first the longest repeating substring
    """

    one_char = set(line)
    if len(one_char) == 1:
        return line

    elements = list(line)
    new = []
    m = 0
    while m < len(elements):
        for n in range(1, len(elements) + 1):
            if m >= n:
                continue
            else:
                new += [''.join(elements[m:n])]
        m += 1

    new_1 = sorted(list(set(new)))
    almost_result = {}

    for s in new_1:
        if line.count(s) > 1:
            almost_result[s] = line.count(s)

    long = 0
    maks = ''
    for al in almost_result.keys():
        le = len(al)
        if len(almost_result.keys()) == 0:
            return ''
        if le > long:
            long = le
            maks = al
        if le == long:
            pass

    try:
        result = str(maks * almost_result[maks])
        if result in line:
            return result
        else:
            result = str(maks * (almost_result[maks] - 1))
            return result
    except KeyError:
        return ''


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')
