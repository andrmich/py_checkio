def get_Fibonacci():
    fib = [0]
    f = 0
    g = 1
    while f < 5000:
        f, g = g, f + g
        fib.append(g)
    return fib


def is_Fibonacci(number):
    return True if number in get_Fibonacci() else False


def checkio(opacity):
    opacity_new = 10000
    y = 0
    if opacity_new == opacity:
        return y
    while opacity_new != opacity:
        y += 1
        if is_Fibonacci(y):
            opacity_new -= y
        else:
            opacity_new += 1
    else:
        return y


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
