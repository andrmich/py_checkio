def f (x):
    y = 1
    for i in range(1, x +1):
        y *= i
    return y

print(f(6) // f(4))
