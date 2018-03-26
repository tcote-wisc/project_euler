"""
Project Euler Problem 003:
    Find the largest prime factor of a given value.

    Ex. The prime factors of 13195 are 5, 7, 13 and 29.

 
"""

def is_prime(num):
    """
    Deterimine if a number is prime
    """
    if num%2 == 0:
        return False

    for i in range(3,num,2):
        if num%i == 0:
            return False

    return True


def find_primes(num):
    """
    Find all primes up to a given number
    """
    primes = []
    for i in range(3,num,2):
        if is_prime(i):
            primes.append(i)
            print(f'{i}\n')

    return primes


if __name__ == "__main__":
    target = 13195

    target_primes = find_primes(target)

    target_fprimes = []

    for prime in target_primes:

        if target%prime == 0:
            target_fprimes.append(prime)

    print(target_fprimes)