from random import randint

def is_prime(n: int) -> bool:
    for i in range(20):
        if not rabin_miller(n):
            return False
    return True

def rabin_miller(n: int) -> bool:
    if n % 2 == 0 or n <= 1:
        return False

    d = n - 1
    while d % 2 == 0:
        d /= 2

    d = int(d)

    a = randint(3, n - 2)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = pow(a, d, n)
        d *= 2
        if x == 1:
            return False
        elif x == n - 1:
            return True
    
    return False