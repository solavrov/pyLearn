from time import time
import multiprocessing


def is_prime(n):
    a = True
    for k in range(2, n):
        if n % k == 0:
            a = False
            break
    print(n, 'is', a)
    return a


if __name__ == '__main__':

    primes = [
        515803,
        326257,
        414283,
        922223,
        431363,
        959461,
        636553,
        230341,
        396353,
        438611,
        894721,
        413533,
        206419,
        214391,
        617777,
        253601,
        289717,
        583181,
        196073,
        247547,
        504631,
        800473,
        209257,
        688573,
        198277,
        173699,
        751123,
        689167,
        147449,
        463247,
        206369,
        130043,
        616207,
        111829,
        884267,
        118169,
        879649,
        480343,
        938507,
        778513,
        986959,
        109367,
        734233,
        408479,
        788369,
        472469,
        991957,
        353237,
        558469,
        313031
    ]

    # single process
    t1 = time()
    for e in primes:
        is_prime(e)
    t2 = time()
    print('one process', t2 - t1)

    # multi processes Process()
    t1 = time()
    processes = []
    for e in primes:
        p = multiprocessing.Process(target=is_prime, args=(e,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    t2 = time()
    print('multi processes Process()', t2 - t1)

    # multi processes Pool()
    t1 = time()
    pool = multiprocessing.Pool()
    pool.map(is_prime, primes)
    pool.close()
    t2 = time()
    print('multi processes Pool()', t2 - t1)
