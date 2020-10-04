from time import time


def is_prime(n):
    t1 = time()
    a = True
    for k in range(2, n):
        if n % k == 0:
            a = False
            break
    t2 = time()
    print(a)
    print(t2 - t1)
    return a


p5 = 72341
p6 = 980957
p7 = 9875813
p8 = 82716217

is_prime(p5)
is_prime(p6)
is_prime(p7)
is_prime(p8)
