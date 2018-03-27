"""
Project Euler Problem 003:
    Find the largest prime factor of a given value.

    Ex. The prime factors of 13195 are 5, 7, 13 and 29.

 """

def trial_division(num):
    out = []  
    while num%2 == 0:
        out.append(2)
        num/=2
    test=3
    while num > 1:
        if (num % test == 0):
            out.append(test)
            num /= test
        else:
            test += 2             
    return out 


if __name__ == "__main__":

     target = 600851475143

     out = trial_division(target)

     print(out)

     import functools
     value = functools.reduce(lambda x,y: x*y, out)

     print(value)


