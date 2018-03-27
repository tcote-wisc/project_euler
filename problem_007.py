"""
Project Euler Problem 007:
    What is the 10001st prime number?

    Ex. By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
    we can see that the 6th prime is 13.
 
"""


def is_prime(num):

    if num == 2:
        return True
    elif num%2 == 0:
        return False

    for i in range(3,num,2):
        if num%i == 0:
            return False

    return True


if __name__ == '__main__':
    
    target = 10001

    primes = []

    check = 2;

    while len(primes) < target:

        if is_prime(check):
            primes.append(check)
            print(len(primes),check)

        check += 1



    print(primes[target])