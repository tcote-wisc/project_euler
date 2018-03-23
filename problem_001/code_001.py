"""
Project Euler Problem 001:
    Find the sum of all the multiples of 3 or 5 below a given value. 
"""

target = 1000;

out = 0;

for val in range(3,target):

    if val%3 == 0 or val%5 == 0:
        out += val

print(f'Sum of multiples for {target} is {out}')
