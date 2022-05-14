from typing import List
from pickle import dump
from calculate_primality import is_prime

def gen_primes(n: int) -> List[int]:
    primes = [2, 3]
    for i in range(5, n):
        if is_prime(i):
            primes.append(i)
    return primes


if __name__ == "__main__":
    num = 100000
    with open(f'primes', 'wb') as f:
        dump(gen_primes(num), f)