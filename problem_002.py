"""
Project Euler Problem 002:
    Find the sum of the even values of the Fibonacci sequence up to a 
    certian value.
"""

target = 4000000;

val1 = 1;
val2 = 2;
out = 0;

while val2 < target:

    if val2%2 == 0:
        out += val2

    temp = val2;
    val2 += val1; 
    val1 = temp;

print(f'Sum of even Fibonacci number up to {target} is {out}')
