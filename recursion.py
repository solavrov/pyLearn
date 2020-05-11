def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def fact2(n):
    if n > 1:
        return n * fact2(n - 1)
    else:
        return 1



