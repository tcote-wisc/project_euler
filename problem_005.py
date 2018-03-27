"""
Project Euler Problem 005:
    What is the smallest positive number that is evenly divisible by all
    of the numbers from 1 to 20?

    Ex. 2520 is the smallest number that can be divided by each of the 
    numbers from 1 to 10 without any remainder
 
"""

target = 20

# brute force method:

val = target
n = target-1

while n > 1:

    if val%n == 0:
        n -= 1
    else:
        val += target
        n = target-1

print(val)


# primes method:

from math import sqrt, floor, log

N = 1
i = 0
check = True
limit = sqrt(target)

p = []
for n in range(2,target):
    for x in range(2,n):
        if n%x == 0:
            break
    else:
        p.append(n)

a = [1 for _ in p]

for i in range(len(p)):
    print(i,p[i])
    if check:
        if p[i] <= limit:
            a[i] = floor( log(target) / log(p[i]) )
        else:
            check = False
    N = N*p[i]**a[i]
    i += 1

print(N)
